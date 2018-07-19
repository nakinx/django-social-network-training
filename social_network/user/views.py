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
       
        # Print how form fields are stored in python variable.
        print(request.POST)

        form = UserForm(request.POST)

        # Print how form should be create on template.
        print(form)

        '''
        The is_valid() function check if the form follow the rules on form, but
        if we want to check if the field are filled correctly we should use
        the function is_bound().
        '''
        if form.is_valid():            
            print('Valid form! Saving data...')

            # Save data about sign user credentials on django default user database.
            new_user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
            
            # Save extension data about the user.
            new_profile = CustomProfile(name = form.data['name'], email = form.data['email'], birthday = form.data['birthday'], credentials = new_user).save()

            return redirect('index')

        print('Invalid form!')

        return render(request, self.template_name, { 'form' : form })