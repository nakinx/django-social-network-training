from django.shortcuts import render, redirect
from custom_profile.models import CustomProfile, FriendInvitation
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print('Index request!')
    
    return render(request, 'custom_profile/index.html', { 'profiles' : CustomProfile.objects.all(), 'logged_profile' : getLoggedProfile(request) })

@login_required
def profile(request, profile_id):
    print('Profile request!')

    return render(request, 'custom_profile/profile.html', { 'profile' : CustomProfile.objects.get(id = profile_id), 'logged_profile' : getLoggedProfile(request) })

@login_required                   
def inviteFriend(request, invited_profile_id):
    print('Invite request!')

    invited_profile = CustomProfile.objects.get(id = invited_profile_id)
    logged_profile = getLoggedProfile(request)
    logged_profile.inviteFriend(invited_profile)
    
    return redirect('index')

@login_required
def acceptFriend(request, invitation_id):
    print('Accept Invitation request!')

    FriendInvitation.objects.get(id = invitation_id).acceptFriend();    

    return redirect('index')

@login_required
def getLoggedProfile(request):
    return request.user.profile  

