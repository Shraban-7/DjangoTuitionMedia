from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
# from accounts.models import Account, Profile, TutionClassDetails, vedio
from .forms import RegistrationForm, LoginForm, AccountUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            # phone_number = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context = {'registration_form': form}
    else:
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'registrations/register.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return render(request, 'registrations/logout.html')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'registrations/login.html', context)


def UpdateAccount(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(initial={
            'email': request.user.email,
            'username': request.user.username,
        })
    context['account_form'] = form
    return render(request, 'registrations/account.html', context)
