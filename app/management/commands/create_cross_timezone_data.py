import arrow

from django.core.management import BaseCommand

from ...models import User, Todo, TIMEZONES


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        This command creates 30 todos going into the future and 30 todos
        going into the past. These todos will cross yesterday's, today's,
        and tomorrow's midnights in each user's timezone.
        """

        for timezone in TIMEZONES:
            user, _ = User.objects.get_or_create(timezone=timezone)

            # create 12, todos crossing midnight (backwards) in some timezones
            for i in range(0, 30):
                past_datetime = arrow.utcnow().to(timezone).shift(hours=-i)
                Todo.objects.get_or_create(user=user, scheduled_datetime=past_datetime.datetime)
                future_datetime = arrow.utcnow().to(timezone).shift(hours=i)
                Todo.objects.get_or_create(user=user, scheduled_datetime=future_datetime.datetime)

        print('created example data')
