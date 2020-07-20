from django.shortcuts import render
from . import forms
#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'We have recieved this form again'
        if form.is_valid():
            html = html + " The Form is Valid"
    else:
        html = 'Welcome for the first time'
    return render(request, 'signup.html', {'html': html, 'form': form})