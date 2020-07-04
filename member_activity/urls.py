from django.urls import path
from . import views

app_name = "member_activity"
urlpatterns = [
    path('', views.MemberListAPIView.as_view(), name="member_api_list_view")
]
