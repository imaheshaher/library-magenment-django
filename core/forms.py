from django import forms
from django.db.models import fields

from core.models import Book, User

class BookForm(forms.ModelForm):
    
    class Meta:
        model=Book
        fields=['book_name','author_name']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["email","password"]



class LoginForm(forms.Form):
    email=forms.EmailField()
    password = forms.CharField()
