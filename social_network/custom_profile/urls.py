from django.urls import path, include
from custom_profile import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'<int:profile_id>/profile', views.profile, name="profile"),
    path(r'<int:invite_profile_id>/invite', views.invite, name="invite"),
]
