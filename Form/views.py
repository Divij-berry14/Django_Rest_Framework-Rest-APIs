from django.shortcuts import render,redirect
from .models import Product
from .forms import *
from django.http import HttpResponse
# from . import forms

#DataFlair #Form #View Functions
def regform(request):
    form = SignUp()
    if request.method == 'POST':
        # print(request.GET)
        print(request.POST) #in dic format
        firstName=request.POST.get("first_name")
        print(firstName)
        form = SignUp(request.POST)
        print(form)
        html = 'We have recieved this form again'
        if form.is_valid():
            print(form.cleaned_data)
            # Product.objects.create(**form.cleaned_data)
            html = html + " The Form is Valid"
        else:
            print(form.errors)
    else:
        html = 'Welcome for the first time'
    return render(request, 'signup.html', {'html': html, 'form': form})


def ProductCreateView(request):
    form=ProductForm(request.POST)
    if form.is_valid():
        print("valid")
        form.save()
        form = ProductForm()
    else:
        print(form.errors)
    context={
        'form':form
    }
    return render(request,"ProductCreate.html",context)

def res(request):
    return HttpResponse("Welcome User")