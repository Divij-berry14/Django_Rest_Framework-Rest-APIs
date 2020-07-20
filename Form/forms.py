from django import forms


# class SignUp(forms.Form):  #subclass of form class
#     firstName=forms.CharField(initial='First Name')
#     lastName=forms.CharField(initial='Last Name')
#     email=forms.CharField(help_text='Write your Email')
#     Address=forms.CharField(required=False,)
#     Technology=forms.CharField(initial='Django',disabled=True)
#     age = forms.IntegerField()
#     password = forms.CharField(widget = forms.PasswordInput)
#     retypePassword = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
#
#     # Validation #DataFlair
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         if len(password) < 4:
#             raise forms.ValidationError("password is too short")
#         return password
from django import forms
from django.core import validators
#DataFlair #Form
class SignUp(forms.Form):
  first_name = forms.CharField(initial = 'First Name', )
  last_name = forms.CharField(required = False)
  email = forms.EmailField(help_text = 'write your email', required = False)
  Address = forms.CharField(required = False, )
  Technology = forms.CharField(initial = 'Django', disabled = True)
  age = forms.IntegerField(required = False, )
  password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
  re_password = forms.CharField(widget = forms.PasswordInput, required = False)