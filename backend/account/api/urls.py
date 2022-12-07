from django.urls import path, include
from account.api.views import (ViewAPIAccountLogin, ViewAPIAccountSignUp, ViewAPIAccountLogout,
                               ViewAPIAccountTokenObtainPair, ViewAPIAccountTokenRefresh)


urlpatterns = [
    path('login/',
         ViewAPIAccountLogin.as_view(),
         name='login'
         ),
    path('signup/',
         ViewAPIAccountSignUp.as_view(),
         name='signup'
         ),

    path('logout/',
         ViewAPIAccountLogout.as_view(),
         name='logout'
         ),

    path('token/', ViewAPIAccountTokenObtainPair.as_view(), name='token_obtain_pair'),
    path('token/refresh/', ViewAPIAccountTokenRefresh.as_view(), name='token_refresh'),

]
