from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class SignupForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields = ('email', 'full_name', 'company_name',)

class ChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = CustomUser
    fields = '__all__'
