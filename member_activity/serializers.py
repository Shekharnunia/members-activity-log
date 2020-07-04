from .models import Member, ActivityPeriod


from rest_framework import serializers


class ActivityPeriodSerializer(serializers.ModelSerializer):

	class Meta:
		model = ActivityPeriod
		fields = [
			"start_time",
			"end_time"
		]


class MemberSerializer(serializers.ModelSerializer):

	activity = ActivityPeriodSerializer(many=True)

	class Meta:
		model = Member
		fields = [
			"id",
			"real_name",
			"tz",
			"activity"
		]