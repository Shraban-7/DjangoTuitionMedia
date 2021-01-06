# from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, AccountUpdateForm

# TOKEN  generator import
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# thirt_party apps

from verify_email.email_handler import send_verification_email

UserModel = get_user_model


# def register_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#
#             # inactive_user = send_verification_email(request, form)
#             user.save()
#             form.save()
#             # email = form.cleaned_data.get('email')
#             # phone_number = form.cleaned_data.get('phone_number')
#             # raw_password = form.cleaned_data.get('password1')
#             # account = authenticate(email=email, password=raw_password)
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('registrations/acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             messages.info(
#                 request, 'Please confirm From your email address to complete the registration and Then you can login')
#             # login(request, account)
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#             # return inactive_user
#     #     # else:
#     #     #     context = {'registration_form': form}
#     else:
#         form = RegistrationForm()
#         # context = {'registration_form': form}
#     return render(request, 'registrations/', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return render(request, 'registrations/logout.html')


# def login_view(request):
#     context = {}
#     # user = request.user
#     # if user.is_authenticated:
#     #     return redirect('/')
#     if request.POST:
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect('/')
#     else:
#         form = LoginForm()
#     context['login_form'] = form
#     return render(request, 'registrations/login.html', context)


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


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registrations/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # 'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.info(
                request, 'Please confirm From your email address to complete the registration and Then you can login')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registrations/register.html', {'form': form})

# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = UserModel._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.info(
#             request, f"Thank you for your email confirmation.  Now you can login your account. {user}")
#         return redirect('login')
#     else:
#         messages.warning(request, 'Activation link is invalid!')
#         return redirect('signup')
