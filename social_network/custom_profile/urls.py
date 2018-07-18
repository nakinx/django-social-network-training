from django.urls import path
from custom_profile import views

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'<int:profile_id>/profile', views.profile, name="profile"),
    path(r'<int:invited_profile_id>/invite-friend', views.inviteFriend, name="invite-friend"),
    path(r'<int:invitation_id>/accept-friend', views.acceptFriend, name="accept-friend"),
]
