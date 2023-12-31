from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')


admin.site.register(Service, ServiceAdmin)
