from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome de usuário',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome de usuário',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'exemplo@email.com',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ao menos 1 letra maiúscula, número e símbolo. Exemplo: Rei@2023',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirme a senha',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))