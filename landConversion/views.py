from django.shortcuts import render

# Create your views here.

def landHome(request):
    return render(request, 'home.html',{'name': 'Ziyad'})