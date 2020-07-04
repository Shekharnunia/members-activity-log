from django.contrib import admin

from .models import Member, ActivityPeriod

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_distplay = ["id", "real_name", "tz"]


@admin.register(ActivityPeriod)
class ActivityPeriodAdmin(admin.ModelAdmin):
	list_distplay = ["id", "member", "start_time", "end_time",]
