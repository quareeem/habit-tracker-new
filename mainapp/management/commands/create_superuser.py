from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
from django.conf import settings

from usersapp.models import CustomUser as User


class Command(BaseCommand):
    help = "Create superuser if it doesn't exist"

    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(
                settings.SUPERUSER_USERNAME,
                settings.SUPERUSER_EMAIL,
                settings.SUPERUSER_PASSWORD
            )
            print(f"""Username: {settings.SUPERUSER_USERNAME},
            Password: {settings.SUPERUSER_PASSWORD}.""")
        else:
            print('User already exists')
