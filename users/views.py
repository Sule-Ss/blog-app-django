from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout, login
from .forms import UserForm, UserProfileForm

from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "home.html")

def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            #! Bütün bilgileri alıp model oluşturur ancak ds e kaydetmez
            profile = form_profile.save(commit=False)
            #! Kullanıcı bilgisini alabilmek için:
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, 'Register Successfull!')

            return redirect('home')

    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }

    return render(request, 'users/register.html',context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        
        if user:
            messages.success(request,'login successfull')
            login(request, user)
            return redirect('home')

    return render(request, 'users/user_login.html', {"form":form})

