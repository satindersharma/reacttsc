import logging


from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls.base import reverse
from account.models import ModelAccountUser
from base.forms import BaseForm

logger = logging.getLogger(__name__)


class FormAccountLogin(BaseForm):
    """User this form to authenticate and login a user
    """

    email = forms.EmailField(
        max_length=225,
        widget=forms.EmailInput(
            attrs = {'placeholder':'Enter your registered email address.'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                'placeholder':'Enter your Password.'
            }
        )
    )

    # ---------------------------------------------------------------------------
    # __init__
    # ---------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormAccountLogin, self).__init__(*args, **kwargs)

    
    # ---------------------------------------------------------------------------
    # clean_email
    # ---------------------------------------------------------------------------
    def clean_email(self):

        email = self.cleaned_data.get('email')

        if email:
            return email.lower()

        return email


    # ---------------------------------------------------------------------------
    # clean
    # ---------------------------------------------------------------------------
    def clean(self):

        invalid_message = 'Invalid username or password'
        try:
            user = ModelAccountUser.objects.get(
                email=self.cleaned_data.get('email')
            )

            if not user.check_password(self.cleaned_data.get('password')):
                raise ObjectDoesNotExist('Invalid username or password')

        except ObjectDoesNotExist:
            raise ValidationError(invalid_message)

        user = authenticate(
            self.request,
            username=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password')
        )

        if not user:
            raise ValidationError(invalid_message)

        if not user.is_active:
            raise ValidationError('Account locked. Please contact support.')

        login(self.request, user)

        data = {
            'email': self.cleaned_data.get('email'),
            'password': self.cleaned_data.get('password')
        }
        logger.info(data)
        user.save()

        return self.cleaned_data



class FormAccountSignup(BaseForm):
    """User use this form to signup """

    first_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name'
            }
        )
    )
    last_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name'
            }
        )
    )
    email = forms.EmailField(
        max_length=225,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password'}
        )
    )
    phone_number = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Phone Number'
            }
        )
    )

    # ---------------------------------------------------------------------------
    # __init__
    # ---------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormAccountSignup, self).__init__(*args, **kwargs)

    def clean_email(self):
        """Make sure that email does not exist."""
        email =  self.cleaned_data.get('email','').lower()

        try:
            ModelAccountUser.objects.get(email=email)
            raise ValidationError(
                ('Email Already exists. <a href="%s">Login instead?</a>') % reverse('account:login')
            )

        except ObjectDoesNotExist:
            pass
        
        return email

    def user_signup(self, request):
        user_data = {
            'email': self.cleaned_data.get('email'),
            'password': self.cleaned_data.get('password'),
            'first_name': self.cleaned_data.get('first_name'),
            'last_name': self.cleaned_data.get('last_name'),
            'phone_number': self.cleaned_data.get('phone_number'),
        }
        ModelAccountUser.objects.signup_process(
            user_data
        )





#  ---------------------------------------------------------------
# FormAccountUserChange
#  ---------------------------------------------------------------
class FormAccountUserChange(forms.ModelForm):
    """
    Form used for updating user information. Includes all the fields in
    the user model, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        )
    )

    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:
        model = ModelAccountUser
        fields = [
            'email', 'first_name', 'last_name', 'is_staff', 'is_superuser',
            'is_active', 'password'
        ]

        

    #  ---------------------------------------------------------------
    # clean_password
    #  ---------------------------------------------------------------
    def clean_password(self):

        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value

        return self.initial["password"]




#  ---------------------------------------------------------------
# FormAccountUserAdmin
#  ---------------------------------------------------------------
class FormAccountUserAdmin(forms.ModelForm):
    """
    A form used for creating new users. Includes all the required
    fields, plus a confirm_password field.
    """

    first_name = forms.CharField(
        max_length=60, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        max_length=60, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    email = forms.EmailField()  # validates email

    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:

        model = ModelAccountUser
        fields = ['email', 'first_name', 'last_name', 'is_staff',
                  'is_superuser', 'is_active']

    #  ---------------------------------------------------------------
    # clean_confirm_password
    #  ---------------------------------------------------------------
    def clean_confirm_password(self):
        """
        This method is used to check whether both the password entries
        match or not.
        """

        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return confirm_password

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------

    def save(self, commit=True):
        """
        This method is used to save the user account's password as
        hashed password.
        """

        user = super().save(commit=False)
        # Updates the user's password as a hashed password
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user