
from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(max_length = 120,label = 'username',
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    password = forms.CharField(
        max_length = 120,widget = forms.PasswordInput(attrs={'placeholder': 'Пароль'}),

    )