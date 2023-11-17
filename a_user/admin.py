from django.contrib import admin

from a_user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'real_name', 'email', 'location', 'bio', ]



