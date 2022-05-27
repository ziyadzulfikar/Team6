from django.shortcuts import render,redirect

from landConversion.models import thaluk, user, village

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
            users = user.objects.filter(thandaperu=thandaperu)
            return render(request, 'land.html', {'users':users})
        else:
            return redirect('/')

def landTypeChange(request):
    if(request.method == 'POST'):
        fieldtype = request.POST["fieldtype"]
        fieldcause = request.POST["fieldcause"]
        landId = request.POST["landId"]

        user.objects.filter(id = landId).update(landAfter=fieldtype, thalukVerification="waiting", villageVerification="waiting thaluk")

        return render(request, 'successful.html')

def thalukOffice(request):
    users = user.objects.filter(thalukVerification = "waiting")
    return render(request, 'Thaluk.html',{'users':users})

def thalukVerified(request):
    user.objects.filter(thalukVerification = "waiting").update(thalukVerification="verified", villageVerification="waiting")
    return render(request, 'successful.html')

def thalukDismiss(request):
    user.objects.filter(thalukVerification = "waiting").update(thalukVerification="dismiss", villageVerification="dismiss")
    return render(request, 'successful.html')

def villageOffice(request):
    users = user.objects.filter(villageVerification = "waiting")
    return render(request, 'village.html',{'users':users})

def villageVerify(request):
    user.objects.filter(villageVerification = "waiting").update(villageVerification="verified")
    user.objects.filter(villageVerification = "waiting").update(villageVerification="verified")

    return render(request, 'successful.html')

def villageDismiss(request):
    user.objects.filter(villageVerification = "waiting").update(villageVerification="dismiss")
    return render(request, 'successful.html')



    
         
