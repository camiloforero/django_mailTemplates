# coding=utf-8
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template 

class MailApi():

    def __init__(self, name):
        email_object = models.Email.objects.get(name=name) #TODO Excepción si no existe
        self.email_object = email_object #TODO: Hacer pruebas de eficiencia

    def send_mail(self, sender, recipients, context=None, cc=None, bcc=None, sender_name=None, attachments=None):
        if cc is None:
            cc = [] 
        if bcc is None:
            bcc = [] 
        if attachments is None:
            attachments = {}
        plainBody = Template(self.email_object.plainBody).render(Context(context))
        htmlBody = Template(self.email_object.htmlBody).render(Context(context))
        email = EmailMultiAlternatives()
        email.subject = Template(self.email_object.subject).render(Context(context))
        email.body = plainBody
        email.attach_alternative(htmlBody, 'text/html')
        email.from_email=sender
        email.to = recipients
        email.cc = cc
        email.bcc = bcc
        for attachment in attachments:
            email.attach(attachment['filename'].encode('ascii', 'ignore'), attachment['data'])
        return email.send()
