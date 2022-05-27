from django.shortcuts import render,redirect
import random
import string
from landConversion.models import land, thaluk,user, village
from django.contrib import messages

# Create your views here.

def landHome(request):
    return render(request, 'home.html',{'name': 'Ziyad'})

def admin(request):
    return render(request, 'admin.html')

def thalukAdmin(request):
    return render(request, 'addTaluk.html')

def villageAdmin(request):
    return render(request, 'addVillage.html')

def addLand(request):
    return render(request, 'addLand.html')

def pay(request):
    return render(request, 'payment.html')

def addUser(request):
    if(request.method == 'GET'):    
            id = ''.join(random.choices(string.digits, k=8))
            thandaperu = id
            name = request.GET["name"]
            location = request.GET["location"]
            pincode = request.GET["pincode"]
            phone = request.GET["phonenumber"]
            adhaar = request.GET["adhaar"]
            userAdd = user.objects.create(thandaperu=thandaperu, name=name, location=location, pincode=pincode, phonenumber=phone, adhaar=adhaar)
            userAdd.save()
            return render(request, 'successful.html')

def addLocation(request):
    if(request.method == 'GET'):    
        location = request.GET["location"]
        pincode = request.GET["pincode"]
        landSize = request.GET["landSize"]
        landBefore = request.GET["landBefore"]
        thandaperu = request.GET["thandaperu"]
        landAdd = land.objects.create(location=location, pincode=pincode, landSize=landSize, landBefore=landBefore, thandaperu=thandaperu)
        landAdd.save()
        return render(request, 'successful.html')

def userlist(request):
    users = user.objects.all()
    return render(request, 'userlist.html', {'users':users})

def addThaluk(request):
    if(request.method == 'GET'):    
            name = request.GET["name"]
            phone = request.GET["phone"]
            place = request.GET["place"]
            pincode = request.GET["pincode"]
            adhaar = request.GET["adhaar"]
            password = request.GET["password"]

            thalukAdd = thaluk.objects.create(name=name, phonenumber=phone, place=place, pincode=pincode, adhaar=adhaar, password=password)
            thalukAdd.save()
            return redirect('/')

def addVillage(request):
    if(request.method == 'GET'):    
            name = request.GET["name"]
            phone = request.GET["phone"]
            place = request.GET["place"]
            pincode = request.GET["pincode"]
            adhaar = request.GET["adhaar"]
            password = request.GET["password"]

            villageAdd = village.objects.create(name=name, phonenumber=phone, place=place, pincode=pincode, adhaar=adhaar, password=password)
            villageAdd.save()
            return redirect('/')

def userAuth(request):
    if(request.method == 'POST'):
        thandaperu = request.POST["thandaperu"]
        adhaar = request.POST["adhaar"]

        verify = user.objects.filter(thandaperu=thandaperu, adhaar=adhaar)

        if(verify):
            users = land.objects.filter(thandaperu=thandaperu)
            return render(request, 'land.html', {'users':users})
        else:
            messages.info(request,'Username already taken')
            print("Invalid Thandaperu or Adhaar Number")
            return redirect('/')

def landTypeChange(request):
    if(request.method == 'POST'):
        fieldtype = request.POST["fieldtype"]
        fieldcause = request.POST["fieldcause"]
        landId = request.POST["landId"]
        landSize = request.POST["landSize"]

        if(int(landSize)<10):
            land.objects.filter(id = landId).update(landAfter=fieldtype, thalukVerification="waiting", villageVerification="waiting thaluk")
            return render(request, 'successful.html')
        else:
            return render(request, 'payment.html')

def thalukOffice(request):
    users = land.objects.filter(thalukVerification = "waiting")
    return render(request, 'Thaluk.html',{'users':users})

def thalukVerified(request):
    if(request.method == 'POST'):
        id = request.POST["id"]
        land.objects.filter(id = id, thalukVerification = "waiting").update(thalukVerification="verified", villageVerification="waiting")
        return render(request, 'successful.html')

def thalukDismiss(request):
    if(request.method == 'POST'):
        id = request.POST["id"]
        land.objects.filter(id = id, thalukVerification = "waiting").update(thalukVerification="dismiss", villageVerification="dismiss")
        return render(request, 'successful.html')

def villageOffice(request):
    users = land.objects.filter(villageVerification = "waiting")
    return render(request, 'village.html',{'users':users})

def villageVerify(request):
    if(request.method == 'POST'):
        id = request.POST["id"]
        landAfter = request.POST["landAfter"]
        land.objects.filter(id = id, villageVerification = "waiting").update(landBefore=landAfter, landAfter="", villageVerification="verified", notification = True)
        return render(request, 'successful.html')

def villageDismiss(request):
    if(request.method == 'POST'):
        id = request.POST["id"]
        land.objects.filter(id = id, villageVerification = "waiting").update(villageVerification="dismiss")
        return render(request, 'successful.html')



    
         
