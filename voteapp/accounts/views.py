from django.forms import DateField
from django.urls import reverse
from .models import CustomUser
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class CustomUserRegistrationForm(UserCreationForm):
    dob = DateField()
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'aadhar', 'kalinga_id']

def index(request):
    return render(request, 'accounts/index.html', {
        'user' : request.user
    })

def login_view(request):
    msg=''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)    
            msg = 'logged in'
            return HttpResponseRedirect(reverse('index'))
        else:
            msg = 'invalid credentials'

    return render(request, 'accounts/login.html', {
        'msg' : msg
    })

def register(request):
    if request.method == 'POST':
        msg = ''
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save()
            msg = 'Registration Successful'
        
    return render(request, "accounts/registration.html", {
        'form':CustomUserRegistrationForm(),
        'msg':msg
    })

def logout_view(request):
    logout(request)
    return render(request, 'accounts/index.html', {
        'msg' : "Logged Out Successfully"
    })