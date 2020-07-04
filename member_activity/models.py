from django.db import models
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Member(models.Model):
	real_name = models.CharField(max_length=120)
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

	def __str__(self):
		return self.real_name


class ActivityPeriod(models.Model):
	member = models.ForeignKey("member_activity.Member", on_delete=models.CASCADE, related_name='activity')
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return self.member.real_name
