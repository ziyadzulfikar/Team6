from django.shortcuts import render,redirect

from landConversion.models import user

# Create your views here.

def landHome(request):
    return render(request, 'home.html',{'name': 'Ziyad'})

def admin(request):
    return render(request, 'admin.html')

def addUser(request):
    if(request.method == 'GET'):    
            thandaperu = request.GET["thandaperu"]
            name = request.GET["name"]
            city = request.GET["city"]
            street = request.GET["street"]
            premises = request.GET["premises"]
            pincode = request.GET["pincode"]
            phone = request.GET["phone"]
            adhaar = request.GET["adhaar"]
            land = request.GET["land"]

            userAdd = user.objects.create(thandaperu=thandaperu, name=name, city=city, street=street, premises=premises, pincode=pincode, phonenumber=phone, adhaar=adhaar, landBefore=land)
            userAdd.save()
            return redirect('/')

def userlist(request):
    users = user.objects.all()
    return render(request, 'userlist.html', {'users':users})