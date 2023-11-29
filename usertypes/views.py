from django.shortcuts import render,HttpResponse,redirect
# from .serializers import *
from .models import *
def home(request):
    return render(request,"index.html")

def main(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        picture=request.FILES.get('picture')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        address=request.POST.get('address')
        type=request.POST.get('type')
        if cpassword==password:
            obj=User.objects.filter(username=uname).first()
            if obj:
                return HttpResponse("Username Already Exists")
            serializer=User(firstname=fname,lastname=lname,picture=picture,username=uname,email=email,password=password,address=address,type=type)
            serializer.save()
            return render(request,"login.html")
        return HttpResponse("Password Didn't Match")

def login(request):
    return render(request,"login.html")
    
def new(request):
    uname=request.GET.get('uname')
    password=request.GET.get('password')
    obj=User.objects.filter(username=uname).first()
    if not obj:
        return HttpResponse("User Not Found!!")
    obj1=User.objects.filter(username=uname,password=password).first()
    if obj1:
        fname=obj1.firstname
        lname=obj1.lastname
        email=obj1.email
        address=obj1.address
        type=obj1.type
        # domain='https://blogupdate-bywb.onrender.com'
        url=str('https://blogupdate-bywb.onrender.com'+obj1.picture.url)
        if type=='Doctor':
            flag=1
            return render(request,"new.html",{'fname':fname,'lname':lname,'email':email,'address':address,'type':type,'url':url,'flag':flag})
        return render(request,"new.html",{'fname':fname,'lname':lname,'email':email,'address':address,'type':type,'url':url})
    else:
        return HttpResponse("Invalid Password!!")
    
def addblog(request):
    return render(request,"add.html")

def upload(request):
    title=request.POST.get('title')
    image=request.FILES.get('image')
    category=request.POST.get('category')
    summary=request.POST.get('summary')
    content=request.POST.get('content')
    obj=Blog(title=title,image=image,category=category,summary=summary,content=content)
    obj.save()
    obj.url=str('https://blogupdate-bywb.onrender.com'+obj.image.url)
    obj.save()
    return redirect("https://blogupdate-bywb.onrender.com/login")

def viewblog(request):
    mental=Blog.objects.filter(category='Mental').all()
    heart=Blog.objects.filter(category='Heart').all()
    covid=Blog.objects.filter(category='Covid').all()
    immunization=Blog.objects.filter(category='Immune').all()
    return render(request,"view.html",{'mental':mental,'heart':heart,'covid':covid,'immune':immunization})
