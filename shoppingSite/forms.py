
from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username'})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password'})
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('User doesnt exist')
            elif not user.check_password(password):
                raise forms.ValidationError('User doesnt exist')
        return super(UserLoginForm, self).clean(*args, **kwargs)
