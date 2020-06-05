from django.shortcuts import render
from .models import  user
from django.http import HttpResponse
# Create your views here.
def index(request):
    message = "Welcome to MeShop you must Login first!!!"
    logout = 0
    params = {'message': message, 'logout': logout}
    return render(request, 'index.html',params)

def success(request,id):
    user_info = user.objects.filter(user_id=id)
    message = "Dashboard !!"
    params = {'id': user_info[0].user_id,
              'username': user_info[0].username,
              'name': user_info[0].name,
              'message':message
              }
    return render(request,'home.html',params)

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        if user.objects.filter(username=username, password=password):
            status_id = user.objects.filter(username=username, password=password).values('user_id', 'username', 'name')
            id = status_id[0]['user_id']
            username = status_id[0]['username']
            name = status_id[0]['name']
            message = "You logged in successfully!!!"
            params = {'id':id,
                      'username': username,
                      'name':name
                      }
            return render(request,'home.html',params)
        else:
            message="Username or passowrd is wrong!!!"
            logout=0
            params={'message':message,'logout':logout}
            return render(request,'index.html',params)

def logout(request):
    message = "You logged out successfully!!!"
    logout = 1
    params = {'message': message, 'logout': logout}
    return render(request,'index.html',params)

def signin(request):
    message = "Sign In here!!!"
    params = {'message': message}
    if request.method =="POST":
        username= request.POST.get("username")
        name= request.POST.get("name")
        password= request.POST.get("password")
        c_password = request.POST.get("password")
        new_user = user(name=name, username=username, password=password)
        new_user.save()
        id=new_user.user_id
        params={'name':name,'username':username,'id':id}
        return render(request,'home.html',params)
    return render(request,'signin.html',params)
