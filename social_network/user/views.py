from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class UserView(TemplateView):
    template_name = 'user/signup.html'

    def post(self, request):
        print("Handling the sign up requisition!")
       
        return redirect('index')