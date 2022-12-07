from django.urls import path, include
from account.api.views import ViewAPIAccountLogin, ViewAPIAccountSignUp, ViewAPIAccountLogout


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

]
