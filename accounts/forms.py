from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import NewUser


# from phonenumber_field.formfields import Phone


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    # phone_number = forms.RegexField(regex=r'^([01]|\+88)?\d{11}', error_messages={
    #     "required": "Phone number must be entered in the format: '+8801000000000'. Up to 15 digits allowed."}
    #                                 )

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid  login")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = NewUser.objects.exclude(
                    pk=self.instance.pk).get(email=email)
            except NewUser.DoesNotExist:
                return email
            raise forms.ValidationError(
                'Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = NewUser.objects.exclude(
                    pk=self.instance.pk).get(username=username)
            except NewUser.DoesNotExist:
                return username
            raise forms.ValidationError(
                'Username "%s" is already in use.' % account.username)
