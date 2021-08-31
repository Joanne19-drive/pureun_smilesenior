from django.contrib import admin
from . import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'phone_number', 'relation', 'complete']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(models.Counseling, UserAdmin)
