from django import forms
from .models import CustomUser

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username", required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)