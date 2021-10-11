from unicodedata import name
from django.urls import path
from . import views

app_name = 'users'
urlpaterns = [
  path('', top, name='Top'),
  path('signup/', SignupView.as_view(), name='Signup'),
  path('login/', LoginView.as_view(), name='Login'),
]