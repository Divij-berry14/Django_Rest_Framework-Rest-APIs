from django import forms
from .models import Product
class SignUp1(forms.Form):  #subclass of form class
    firstName=forms.CharField(initial='First Name')
    lastName=forms.CharField(initial='Last Name')
    email=forms.CharField(help_text='Write your Email')
    Address=forms.CharField(required=False,)
    Technology=forms.CharField(initial='Django',disabled=True)
    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput)
    retypePassword = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)

    # Validation #DataFlair
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

# from django import forms
from django.core import validators
#DataFlair #Form
class SignUp(forms.Form):
  #formFields
  first_name = forms.CharField(initial = 'First Name', )
  last_name=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
  email = forms.EmailField(help_text = 'write your email', required = False)
  Address = forms.CharField(required = False,widget=forms.Textarea)
  Technology = forms.CharField(initial = 'Django', disabled = True)
  age = forms.IntegerField(required = False, )
  password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
  re_password = forms.CharField(widget = forms.PasswordInput, required = False)


class ProductForm(forms.ModelForm):  #ModelForm
  title=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Title'}))    #override the title field
  class Meta:
    model = Product
    fields = ['title','description','price']

  def clean_title(self,*args,**kwargs):
    title=self.cleaned_data['title']
    # print(title)
    if not "CFE" in title:
      return forms.ValidationError("This is not valid title")
    else:
      return title
