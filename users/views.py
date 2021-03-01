from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created!')
            return redirect("/login")

    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
