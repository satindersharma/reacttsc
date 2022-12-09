import logging

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from account.models import ModelAccountUser


logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# SerializerAPIAccountLogin
# ---------------------------------------------------------------
class SerializerAPIAccountLogin(serializers.Serializer):
    """
    Represents login data.
    """

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30)

    # ---------------------------------------------------------------
    # validate
    # ---------------------------------------------------------------
    def validate(self, attrs):

        try:
            email = attrs['email'].lower()
            self.user = ModelAccountUser.objects.get(email=email)

        except (ObjectDoesNotExist, AttributeError):
            raise serializers.ValidationError(
                'Invalid email, Please check and try again.')

        if not self.user.check_password(attrs['password']):
            raise serializers.ValidationError(
                'Invalid password, Please check and try again.')

        return serializers.Serializer.validate(self, attrs)

    # ---------------------------------------------------------------
    # login
    # ---------------------------------------------------------------
    def login(self):
        login_user = ModelAccountUser.objects.login_user(
            self.user, self.context['request'],
            self.validated_data['password']
        )
        
        return login_user


# ---------------------------------------------------------------
# SerializerAccountSignUp
# ---------------------------------------------------------------
class SerializerAPIAccountSignUp(serializers.Serializer):

    """
    Register as User
    """

    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=60)
    phone_number = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30, required=False)
    city = serializers.CharField(max_length=30, required=False)

    #  ---------------------------------------------------------------
    # validate_email
    #  ---------------------------------------------------------------

    def validate_email(self, email):
        """
        Make sure emails are unique.
        """

        email = email.lower()

        try:
            ModelAccountUser.objects.get(email=email)
            raise serializers.ValidationError(
                'Email {} already exists. Please choose another one.'.format(
                    email)
            )
        except ObjectDoesNotExist:
            return email

    # ---------------------------------------------------------------
    # validate_phone_number
    # ---------------------------------------------------------------

    def validate_phone_number(self, phone_number):
        """
        Make sure phone_numbers are unique.
        """
        try:
            ModelAccountUser.objects.get(phone_number=phone_number)
            raise serializers.ValidationError(
                'Phone {} already exists. Please choose another one.'.format(
                    phone_number)
            )
        except ObjectDoesNotExist:
            return phone_number

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self):

        user_data = {
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),
            'phone_number': self.validated_data.get('phone_number'),
            'country': self.validated_data.get('country'),
            'city': self.validated_data.get('city'),
        }

        user = ModelAccountUser.objects.signup_process(
            user_data
        )
        return SerializerAPIAccountUser(user).data


# ---------------------------------------------------------------
# SerializerAccountUser
# ---------------------------------------------------------------
class SerializerAPIAccountUser(serializers.ModelSerializer):

    class Meta:
        model = ModelAccountUser
        fields = ('id', 'first_name', 'last_name', 'uid', 'phone_number')


# ---------------------------------------------------------------
# SerializerAPIAccountLogout
# ---------------------------------------------------------------
class SerializerAPIAccountLogout(serializers.Serializer):
    """
    Represents login data.
    """

    pass
