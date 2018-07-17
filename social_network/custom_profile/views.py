from django.shortcuts import render, redirect
from custom_profile.models import CustomProfile

def index(request):
    print('Index request!')

    profile1 = CustomProfile.objects.get(id = 1)
    print(profile1)

    return render(request, 'index.html', { 'profiles' : CustomProfile.objects.all() })

def profile(request, profile_id):
    print('Profile request!')

    return render(request, 'profile.html', { 'profile' : CustomProfile.objects.get(id = profile_id)})

def invite(request, invite_profile_id):
    print('Invite request!')

    invite_profile = CustomProfile.objects.get(id = invite_profile_id)
    logged_profile = getLoggedProfile(request)
    
    return redirect('index')

def getLoggedProfile(request):
    return CustomProfile.objects.get(id = 1)

