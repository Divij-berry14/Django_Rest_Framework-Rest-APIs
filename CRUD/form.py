from Crud.models import Book
from django import forms

class BookCreate(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
