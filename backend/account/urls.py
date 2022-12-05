from django.urls import path
from account.views import ViewAccountLogin, ViewAccountSignup, ViewAccountLogout, ViewAccountDashboard

urlpatterns = [
    path("", ViewAccountLogin.as_view(), name="login"),
    path("signup/", ViewAccountSignup.as_view(), name="signup"),
    path("logout/", ViewAccountLogout.as_view(), name="logout"),
    path("dashboard/", ViewAccountDashboard.as_view(), name="dashboard"),
]
