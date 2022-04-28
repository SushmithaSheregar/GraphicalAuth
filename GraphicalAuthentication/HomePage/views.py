from django.shortcuts import render
from HomePage.models import Details

# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == "POST":
        Username=request.POST['Username']
        email = request.POST['email']
        phone = request.POST['phone']
        img_index = request.POST['img_index']
        ins2 = Details(img_index=img_index, Username=Username, email=email, phone=phone)
        ins2.save()
        print("data entered")
    return render(request, 'signup.html')
