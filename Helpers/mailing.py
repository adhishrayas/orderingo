from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context
from django.template.loader import get_template
from ord.settings import EMAIL_HOST_USER
from Users.models import CustomUser
from django.template.loader import render_to_string


@receiver(post_save,sender = CustomUser)
def send_profile_mail(sender,instance,**kwargs):
    htmly = "email.html"
    recipientlist = list(CustomUser.objects.all().values_list("email",flat = True))
    html_content = (htmly,{'heading':"Hi" + instance.email,})
    mail = EmailMultiAlternatives(
        subject = "Thank you for using our website!",
        body = html_content,
        from_email=EMAIL_HOST_USER,
        bcc = recipientlist,
        reply_to=[EMAIL_HOST_USER],
    )
    mail.content_subtype = "html"
    mail.send()