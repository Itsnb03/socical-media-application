from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import profile

# Create your views here.

def signup(request):
    try:
        if request.method == 'POST':
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            my_user = User.objects.create_user(fnm,emailid,pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = profile.objects.create(user=user_model,id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request,my_user)
                return redirect('/')
            return redirect('/')
    except:
        invalid="User Already Exists"
        return render(request,'signup.html',{'invalid':invalid})


def home(request):
    return HttpResponse("<h1>Hello</h1>")



