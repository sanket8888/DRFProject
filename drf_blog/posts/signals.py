from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post

@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'New post created: {instance.title}'
        message = f'Hi {instance.author.username},\n\nA new post "{instance.title}" has been created.\n\nThanks!'
        send_mail(
            subject,
            message,
            'noreply@example.com',
            [instance.author.email],
            fail_silently=False,
        )
