from django.urls import path
from . import views

from .views import  SignUpUser


app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', SignUpUser.as_view(), name='signup'),
]


