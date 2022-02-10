from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content= request.POST['content']
        print(name,email,phone,content)
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request,'home/contact.html')

def videos(request):
    return render(request,'home/videos.html')

def login(request):
    if request.method=='POST':
        email= request.POST['email']
        password= request.POST['password']
        print(email,password)
        login = Login(email=email, password=password)
        login.save()
    return render(request,'home/login.html')

def signup(request):
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        content= request.POST['content']
        print(name,email,phone,content)
        signup = Signup(name=name, email=email, phone=phone, content=content)
        signup.save()
    return render(request,'home/signup.html')