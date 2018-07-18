from django.shortcuts import render, redirect
from custom_profile.models import CustomProfile, FriendInvitation

def index(request):
    print('Index request!')
    
    return render(request, 'custom_profile/index.html', { 'profiles' : CustomProfile.objects.all(), 'logged_profile' : getLoggedProfile(request) })

def profile(request, profile_id):
    print('Profile request!')

    return render(request, 'custom_profile/profile.html', { 'profile' : CustomProfile.objects.get(id = profile_id), 'logged_profile' : getLoggedProfile(request) })
                                           
def inviteFriend(request, invited_profile_id):
    print('Invite request!')

    invited_profile = CustomProfile.objects.get(id = invited_profile_id)
    logged_profile = getLoggedProfile(request)
    logged_profile.inviteFriend(invited_profile)
    
    return redirect('index')

def acceptFriend(request, invitation_id):
    print('Accept Invitation request!')

    FriendInvitation.objects.get(id = invitation_id).acceptFriend();    

    return redirect('index')

def getLoggedProfile(request):
    return CustomProfile.objects.get(id = 4)   

