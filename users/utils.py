from django.core.mail import send_mail
from django.conf import settings


def send_verification_email(user):
    subject = 'Подтверждение адреса электронной почты'
    message = f'Приветствуем {user.email},' \
              f' пожалуйста, подтвердите свой адрес электронной почты, нажав на эту ссылку:' \
              f' http://localhost:8000/verify/{user.pk}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
