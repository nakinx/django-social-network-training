from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(required=True, max_length=150)    
    password = forms.CharField(required=True, max_length=128)
    name = forms.CharField(required=True, min_length=4, max_length=256)
    email = forms.EmailField(required=True)
    birthday = forms.DateField(required=True)

    '''
    This method is for training purpose and it objetive is to not allow
    username containing number.
    '''    
    def clean_username(self):
        # Get the field username already treated.
        username = self.cleaned_data['username']

        if not username.isalpha():
            raise forms.ValidationError(_('You should not use number in username.'), code='invalid')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('Username already in use.'), code='invalid')

        return username
