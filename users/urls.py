from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    # path('login/', obtain_auth_token, name='login'),
    path('login/', views.LoginView.as_view()),
]
