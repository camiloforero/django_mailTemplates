# coding=utf-8
from django.contrib import admin
from .models import Email, Attachment

class AttachmentInline(admin.TabularInline):
    model = Attachment

@admin.register(Email)
class MailAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]

# Register your models here.
