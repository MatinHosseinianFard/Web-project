from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
        self.fields['password1'].widget.attrs['placeholder'] = 'رمز'
        self.fields['password2'].widget.attrs['placeholder'] = 'تکرار رمز'


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['password'].widget.attrs['placeholder'] = 'رمز'