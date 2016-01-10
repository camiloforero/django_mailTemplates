# coding=utf-8
from . import models
from django.core.mail import send_mail
from django.template import Context, Template 

class MailApi():

    def __init__(self, name):
        email = models.Email.objects.get(name=name) #TODO Excepción si no existe
        self.email = email #TODO: Hacer pruebas de eficiencia

    def send_mail(self, sender, recipients, cc=None, bcc=None, context=None, sender_name=None):
        plainBody = Template(self.email.plainBody).render(Context(context))
        htmlBody = Template(self.email.htmlBody).render(Context(context))
        send_mail(self.email.subject, plainBody, sender, recipients, fail_silently=False, html_message = htmlBody) #Agregar cc y bcc y html y archivos adjuntos
        



