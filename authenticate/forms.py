from django import forms


class UserLoginForm(forms.Form):
    login = forms.CharField(required=False)
    password = forms.CharField(required=False, initial=False, widget=forms.PasswordInput)