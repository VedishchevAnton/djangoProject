# кастомная команда создания суперпользователя
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(

            email='Brando',
            first_name='Anton',
            last_name='Vedishev',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('Q1w2e3r4')
        user.save()
