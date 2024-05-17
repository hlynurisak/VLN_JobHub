from django.contrib import admin
from django.contrib.auth.models import User

from application.models import Application


# Register your models here.
admin.site.register(Application)

