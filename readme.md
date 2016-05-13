THis module was created to easily send templated e-mails programmatically. It uses python's default email backend. It is recommended to use Mailgun's backend for added functionality

The emails are created with an unique name, their html and raw text (with variable fields surrounder with {{ }} like a normal django template. Then, it is just a matter of calling them by name, and sending as many as necessary, each with their own senders, recipients and context
