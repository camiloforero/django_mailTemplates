# coding=utf-8
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template 

class MailApi():

    def __init__(self, name):
        email_object = models.Email.objects.get(name=name) #TODO Excepción si no existe
        self.email_object = email_object #TODO: Hacer pruebas de eficiencia

    def send_mail(self, sender, recipients, context=None, cc=None, bcc=None, sender_name="", attachments=None):
        """
        This method sends the mail with the given parameters, replacing any variable fields with those in the context
        """
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
        email.from_email="%s <%s>" %(sender_name, sender)
        email.to = recipients
        email.cc = cc
        email.bcc = bcc
        for attachment in self.email_object.attachments.all():
            email.attach("%s.%s" % (attachment.name, attachment.fileAttachment.file.name.split(".")[-1]), attachment.fileAttachment.file.read())
        for attachment in attachments:
            email.attach(attachment['filename'].encode('ascii', 'ignore'), attachment['data'])
        email.tags = map(unicode.strip, self.email_object.tags.split(','))
        email.track_clicks = True
        return email.send()
