from django import forms
from .models import Talk

class TalkForm(forms.ModelForm):
  class Meta:
    model = Talk
    fields = (
      'content', 'created_at'
    )

# class RoomForm(forms.ModelForm):
#   class Meta:
#     model = Room
#     field = '__all__'