from django import forms
from .models import Board
from django.contrib.auth.forms import UserCreationForm
from .validation import validate_email, validate_password
# class DateInput(forms.DateInput):
#     input_type = 'date'

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('b_title', 'b_note')
        # widgets = {
        #     'end_date' : DateInput()
        # }


class UserRegisterForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']

    username       = forms.CharField(
        max_length = 15,
    )
    email          = forms.EmailField(
        max_length = 50,
        validators = [validate_email],
        # unique     = True,
    )
    password1       = forms.CharField(
        max_length = 300,
        validators = [validate_password],
        min_length= 8
    )

    password2       = forms.CharField(
        max_length = 300,
        validators = [validate_password],
        min_length= 8
    )





# class RegisterForm(forms.Form):
#     username = forms.CharField(
#         max_length=20,
#         min_length=3,
#     )
#     email = forms.EmailField
#     password1 = forms.CharField(write_only=True)
#     password2 = forms.CharField(write_only=True)

