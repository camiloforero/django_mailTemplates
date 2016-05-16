THis module was created to easily send templated e-mails programmatically. It uses python's default email backend. It is recommended to use Mailgun's backend for added functionality

The emails are created with an unique name, their html and raw text (with variable fields surrounder with {{ }} like a normal django template. Then, it is just a matter of calling them by name, and sending as many as necessary, each with their own senders, recipients and context

This module also requires the django_wysiwyg editor. Install it via
Installation:
pip install django-wysiwyg
pip install django-tinymce
Add django_mailTemplates ,django_wysiwyg and tinymce to installed apps
Add tinymce.urls to urls.py (https://github.com/aljosa/django-tinymce)

Add the following to the project settings
DJANGO_WYSIWYG_FLAVOR = "tinymce"    # or "tinymce_advanced"


