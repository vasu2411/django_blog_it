from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .models import Users

def register(request):
    return render(request,"userauth/register.html")

def login(request):
    return render(request,"userauth/login.html")

def endecryptPassword(password,mode):
    translated=""
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in password:
        if i in alpha:
            num = alpha.find(i)
            if mode=="encrypt":
                num=num+3
            elif mode=="decrypt":
                num=num-3

            if num >= len(alpha):
                num=num-len(alpha)
            elif num < 0:
                num=num+len(alpha)
            translated=translated+alpha[num]
        else:
            translated=translated+i

    return translated

def registernewuser(request):

    if request.POST:
        data = request.POST.copy()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        emailid = data.get('emailid')
        password = data.get('password')
        confirmpassword = data.get('confirmpassword')

        count=0

        if password == confirmpassword:
            users = Users.objects.all()

            for user in users:
                if user.email_id==emailid:
                    count=1
                    messages.error(request, 'It seems you already registered on the system.')
                    return redirect('/register')

            if count==0:
                encrypted_password = endecryptPassword(password,"encrypt")
                user = Users.objects.create(first_name=firstname, last_name=lastname, email_id=emailid, password=encrypted_password)
                user.save()
                messages.success(request, 'Registered successfully')
                return redirect('/index')
        else:
            messages.error(request, 'Password and Confirm-password must be equal')
            return redirect('/register')

def userlogin(request):

    if request.POST:
        data = request.POST.copy()
        emailid = data.get('emailid')
        password = data.get('password')
        users = Users.objects.all()

        for user in users:
            if user.email_id==emailid:
                decrypted_password=endecryptPassword(user.password,"decrypt")
                if password==decrypted_password:
                    return redirect('./posts')

def home(request):
    return redirect('/posts/index')