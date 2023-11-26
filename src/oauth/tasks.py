from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_email_message_task(username, email):
    send_mail(
        'Регистрация',
        f'Добро пожаловать, {username}! Вы успешно зарегистрировались.',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
