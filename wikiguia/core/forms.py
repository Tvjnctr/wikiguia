from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Tu Usuario',
        'class':'input_form_box',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Tu correo',
        'class':'input_form_box',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Ingresa Contraseña',
        'class':'input_form_box',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repite la Contraseña',
        'class':'input_form_box',
    }))