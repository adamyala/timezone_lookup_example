import arrow

from django.core.management import BaseCommand

from ...models import User, Todo, TIMEZONES


class Command(BaseCommand):
    def handle(self, *args, **options):

        for timezone in TIMEZONES:
            user, _ = User.objects.get_or_create(timezone=timezone)

            # create 12, todos crossing midnight (backwards) in some timezones
            for i in range(1, 24):
                scheduled_datetime = arrow.utcnow().to(timezone).shift(hours=-i)
                Todo.objects.get_or_create(user=user, scheduled_datetime=scheduled_datetime.datetime)
