# coding=utf-8
from __future__ import unicode_literals

from django.db import models

class Email(models.Model):
    """
        This class models an email and all necessary information to make one.

        Users will be intended to create a database instance of this model by using the admin or by creating their own views. Later on, they will be able to call it by name and use it as a template for the emails they want to send
    """
    name = models.CharField(max_length=64, unique=True) #TODO: help_text and create an index on this field
    subject = models.CharField(max_length=128)
    plainBody = models.TextField()
    htmlBody = models.TextField(blank=True, null=True)
    campaignName = models.CharField(blank=True, null=True, max_length = 32) #TODO: leer sobre campañas en mailgun, ver el tamaño máximo, agregar texto de ayuda
    tags = models.CharField(blank=True, null=True, max_length=64, help_text="Insert all tags separated by a comma.")
    def __str__(self):
        return self.name + ' - ' + self.subject

class Attachment(models.Model):
    name = models.CharField(max_length=32)
    fileAttachment = models.FileField()
    email=models.ForeignKey(Email, models.CASCADE, related_name='attachments')



# Create your models here.
