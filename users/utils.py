from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings


# def generate_email_verification_token(user):
#     """Функция, которая будет генерировать токен для верификации почты"""
#     return default_token_generator.make_token(user)
#
#
# def send_email_verification_mail(user):
#     """Функция, которая будет отправлять письмо с токеном для верификации почты."""
#     token = user.generate_email_verification_token(user)
#     subject = 'Подтверждение адреса электронной почты'
#     message = f'Пожалуйста, нажмите на следующую ссылку, чтобы подтвердить свой адрес электронной почты:' \
#               f' {settings.BASE_URL}/email-verification/?token={token}'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     recipient_list = [user.email]
#     send_mail(subject, message, from_email, recipient_list)


def send_verification_email(user):
    subject = 'Подтверждение адреса электронной почты'
    message = f'Приветствуем {user.username},' \
              f' пожалуйста, подтвердите свой адрес электронной почты, нажав на эту ссылку:' \
              f' http://localhost:8000/verify/{user.pk}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
