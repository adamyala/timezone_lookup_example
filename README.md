# timezone_lookup_example

```
docker compose build
docker compose up
poetry run python manage.py create_cross_timezone_data
```

PSQL query to return all TODOs after their scheduled time but still today in the user's timezone
```
select 
	t.id,
	t.scheduled_datetime,
	u.timezone,
	t.scheduled_datetime at time zone u.timezone as localized_datetime,
	date_trunc('day', t.scheduled_datetime at time zone u.timezone) + interval '23 hours 59 minutes'
from app_todo as t
join app_user as u on t.user_id = u.id
where 
	t.scheduled_datetime at time zone u.timezone < date_trunc('day', now() at time zone u.timezone) + interval '23 hours 59 minutes'
	and t.scheduled_datetime at time zone u.timezone > date_trunc('day', now() at time zone u.timezone)
```
