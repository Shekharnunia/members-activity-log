from django.shortcuts import render

from rest_framework import generics

from .models import Member, ActivityPeriod
from .serializers import MemberSerializer


class MemberListAPIView(generics.ListAPIView):
	serializer_class = MemberSerializer
	queryset = Member.objects.order_by("-id").prefetch_related("activity")
	