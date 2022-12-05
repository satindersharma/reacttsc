import logging
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.urls.base import reverse
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from account.forms import FormAccountLogin, FormAccountSignup
from django.conf import settings


logger = logging.getLogger(__name__)


class ViewAccountLogin(SuccessMessageMixin, FormView):
    """
    Use this view to login
    """
    form_class = FormAccountLogin

    template_name = "account/login.html"

    # ---------------------------------------------------------------------------
    # get
    # ---------------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.DEFAULT_LOGIN_REDIRECT_URL)

        return FormView.get(self, request, *args, **kwargs)

    # ---------------------------------------------------------------------------
    # get_form_kwargs
    # ---------------------------------------------------------------------------
    def get_form_kwargs(self):
        kwargs = FormView.get_form_kwargs(self)
        kwargs['request'] = self.request
        return kwargs

    # ---------------------------------------------------------------------------
    # form_valid
    # ---------------------------------------------------------------------------
    def form_valid(self, form):
        """
        Login and redirect the user to the default redirect url.
        """
        url = settings.DEFAULT_LOGIN_REDIRECT_URL

        logger.debug('Redirecting %s to %s', self.request.user, url)

        return redirect(url)


class ViewAccountSignup(SuccessMessageMixin, FormView):
    """
    Use this view to signup.
    """

    form_class = FormAccountSignup
    template_name = 'account/signup.html'
    success_url = settings.LOGIN_URL

    # ---------------------------------------------------------------------------
    # get
    # ---------------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.DEFAULT_LOGIN_REDIRECT_URL)

        return FormView.get(self, request, *args, **kwargs)

    # ---------------------------------------------------------------------------
    # get_form_kwargs
    # ---------------------------------------------------------------------------
    def get_form_kwargs(self):
        kwargs = FormView.get_form_kwargs(self)
        kwargs['request'] = self.request
        return kwargs

    # ---------------------------------------------------------------------------
    # form_invalid
    # ---------------------------------------------------------------------------
    def form_invalid(self, form):
        """
        Login and redirect the user to the default redirect url.
        """
        
        return FormView.form_invalid(self, form)

    # ---------------------------------------------------------------------------
    # form_valid
    # ---------------------------------------------------------------------------
    def form_valid(self, form):
        """
        Perform user signup process
        """
        form.user_signup(self.request)
        return FormView.form_valid(self, form)



class ViewAccountLogout(RedirectView):
    """
    View to handle logout process.
    """

    # ---------------------------------------------------------------------------
    # get_redirect_url
    # ---------------------------------------------------------------------------
    def get_redirect_url(self, *args, **kwargs):
        """
        Method to logout user and redirect it to the login screen.
        """
        logout(self.request)

        return reverse('account:login')



class ViewAccountDashboard(TemplateView):
    template_name = 'account/dashboard.html'

    # ---------------------------------------------------------------------------
    # get
    # ---------------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account:login'))

        return TemplateView.get(self, request, *args, **kwargs)
