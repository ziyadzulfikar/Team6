from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.landHome, name = 'landHome'),
    path('adminView', views.admin, name = 'admin'),
    path('addUser', views.addUser, name = 'addUser'),
    path('userlist', views.userlist, name = 'userlist'),
]