from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):

    usernamex = forms.CharField(required=True)

    
    def is_valid(self):
        is_valid_form = True

        print(usernamex)

        print(self)
        if not super(UserForm, self).is_valid():
            print('porra2')            
            self.addErrorMsg('Please check the inserted values.')
            is_valid_form = False
        
        print(is_valid_form)

        # Check if the username is unique.
        #if User.objects.filter(username = self.data['username']).exists():
        #    self.addErrorMsg('Username already in use.')
        #    is_valid_form = False

        return is_valid_form

    def addErrorMsg(self, msg):
        self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList()).append(msg)

    def __str__(self):
        return "{} {} {} {} {}".format(self.usernamex, self.password, self.name, self.email, self.birthday)
