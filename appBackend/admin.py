from django.contrib import admin
from .models import Room, Talk

# Register your models here.

appFunction = [Room, Talk]

admin.site.register(appFunction)