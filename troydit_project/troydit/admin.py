from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm, CustomUserChangeForm
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'image_url', 'description']

admin.site.register(User, CustomUserAdmin)
