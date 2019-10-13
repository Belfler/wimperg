from django.contrib import admin

from wimperg.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'date_of_birth')
