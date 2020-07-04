import random, pytz

from django.core.management.base import BaseCommand
from member_activity.models import Member, ActivityPeriod

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Popular members in database'

    def handle(self, *args, **kwargs):
    	for i in range(50):
    		member = Member.objects.create(real_name=fake.name(), tz=random.choice(pytz.all_timezones))
    		for i in range(4):
    			start_time = fake.date_time()
    			end_time = fake.date_time_between(start_date=start_time, end_date=random.randint(1,30))
    			ActivityPeriod.objects.create(member=member, start_time=start_time, end_time=end_time)