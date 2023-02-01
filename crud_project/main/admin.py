from django.contrib import admin
from .models import Patient, Doctor

# Register your models here.
class JugadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created','edited')

admin.site.register(Patient)
admin.site.register(Doctor)