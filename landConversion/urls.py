from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.landHome, name = 'landHome'),
    path('adminView', views.admin, name = 'admin'),
    path('addUser', views.addUser, name = 'addUser'),
    path('userlist', views.userlist, name = 'userlist'),
    path('addThaluk', views.addThaluk, name = 'addThaluk'),
    path('addVillage', views.addVillage, name = 'addVillage'),
    path('userAuth', views.userAuth, name = 'userAuth'),
    path('landTypeChange', views.landTypeChange, name = 'landTypeChange'),
    path('thalukOffice', views.thalukOffice, name = 'thalukOffice'),
    path('thalukVerified', views.thalukVerified, name = 'thalukVerified'),
    path('thalukDismiss', views.thalukDismiss, name = 'thalukDismiss'),
    path('villageOffice', views.villageOffice, name = 'villageOffice'),
    path('villageVerify', views.villageVerify, name = 'villageVerify'),
    path('villageDismiss', views.villageDismiss, name = 'villageDismiss'),
]