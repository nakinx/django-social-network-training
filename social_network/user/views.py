from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from user.forms import UserForm
from custom_profile.models import CustomProfile

class UserView(View):
    template_name = 'user/signup.html'

    def get(self, request):
        print("Handling GET request to sign up!")

        return render(request, self.template_name)

    def post(self, request):
        print("Handling POST request to sign up!")
       
        form = UserForm(request.POST)

        if form.is_valid():
            
            # Save data about sign user credentials on django default user database.
            new_user = User.objects.create_user(form.data['name'], form.data['email'], form.data['password'])

            print(new_user)

            # Save extension data about the user.
            new_profile = CustomProfile(name = form.data['name'], email = form.data['email'], birthday = form.data['birthday'], user = new_user).save()

            print(new_profile)

            return redirect('index')

        print('fudeu')

        return render(request, self.template_name, { 'form' : form })