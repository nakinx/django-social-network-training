from django.urls import path
from user.views import UserView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'signup', UserView.as_view(), name='signup'),
    path(r'signin', auth_views.login, {'template_name':'user/signin.html'}, name='signin'),
    path(r'signout', auth_views.logout_then_login, name='signout')
]
