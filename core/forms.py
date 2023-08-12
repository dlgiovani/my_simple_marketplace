from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Hey, who are you? Tell me your username.',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '- It didn\'t work? \n- Impossible! That is password! That is... Oh, no! Caps Lock.',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Choose your username ^-^',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'example@email.com',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create a <strong> password for yourself',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Can you remember the password you typed above? Let\'s check.',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))