from django.contrib import admin

from backend.authentication.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)