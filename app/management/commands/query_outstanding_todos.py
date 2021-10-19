from django.core.management import BaseCommand

from ...models import User, Todo


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
