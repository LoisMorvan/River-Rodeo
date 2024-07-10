from django.contrib import admin

from backend.authentication.models import CustomUser, Friendship

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Friendship)