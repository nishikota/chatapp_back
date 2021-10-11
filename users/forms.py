from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['email'].widget.attrs['class'] = 'form-control'
      self.fields['first_name'].widget.attrs['class'] = 'form-control'
      self.fields['last_name'].widget.attrs['class'] = 'form-control'
      self.fields['company_name'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['class'] = 'form-control'

  class Meta:
    model = CustomUser
    fields = ('email', 'first_name', 'last_name', 'company_name', 'password1', 'password2')

class LoginForm(forms.Form):
  email = forms.EmailField(label='メールアドレス', max_length=100)
  first_name = forms.CharField(label='名', max_length=50)
  last_name = forms.CharField(label='姓', max_length=50)
  company_name = forms.CharField(label='会社名', max_length=100)
  password = forms.CharField(
    label=('password'),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    help_text=password_validation.password_validators_help_text_html(),
  )

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['email'].widget.attrs['class'] = 'form-control'
      self.fields['password'].widget.attrs['class'] = 'form-control'