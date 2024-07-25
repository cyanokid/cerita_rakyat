from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#library for register
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


# Create your views here.
def login_user(request):

    #if they fill the form
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ("Anda Sudah Berjaya Masuk Ke Akaun Anda."))
            return redirect('home')

        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Kata Nama atau Kata Laluan Anda Tidak Sah. Sila Cuba Lagi. "))
            return redirect('login')

    #return an 'invalid login' error
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request, ("Anda Sudah Keluar Dari Akaun Anda."))
    return redirect('home')

def register_user(request):
    #if they fill up the form
    if request.method == "POST":
        #the form is filled and submit
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #to sign in after sign up the form
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Pendaftaran Berjaya! "))
            return redirect('home')
            
    #if they want to fill up the form/ not yet fill up the form
    else:
        #pass the blank form
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {
        "form" : form,
    })