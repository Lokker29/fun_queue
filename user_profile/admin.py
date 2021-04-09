from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import User, Faculty, UniGroup

admin.site.register(User, BaseUserAdmin)
admin.site.register(Faculty)
admin.site.register(UniGroup)
