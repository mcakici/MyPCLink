from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserRegisterForm
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == 'POST':
        user_creation_form = UserRegisterForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.success(request, 'Your account has been created. You are now able to log in.')
            return redirect('login')
    else:
        user_creation_form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': user_creation_form})
