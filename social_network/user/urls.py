from django.urls import path
from user.views import UserView

urlpatterns = [
    path(r'signup', UserView.as_view(), name='signup')    
]
