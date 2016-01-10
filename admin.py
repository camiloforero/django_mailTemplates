# coding=utf-8
from django.contrib import admin
from .models import Email

@admin.register(Email)
class AplicacionAdmin(admin.ModelAdmin):
    pass


# Register your models here.
