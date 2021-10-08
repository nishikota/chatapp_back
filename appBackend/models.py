from email import contentmanager
from djongo import models
from django.utils import timezone
from users.models import CustomUser


# Create your models here.

class Talk(models.Model):
  # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  # title = models.CharField(max_length=50, null=True)
  content = models.CharField(max_length=500, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return (f'{self.created_at}')
  class Meta:
    abstract = True


class Room(models.Model):
  user = models.ManyToManyField(CustomUser)
  name = models.CharField('ルーム名', max_length=100)
  from .forms import TalkForm
  talk = models.EmbeddedField(
    model_container = Talk,
    model_form_class = TalkForm,
  )
  objects = models.DjongoManager()
  # talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
  def __str__(self):
    return self.name


