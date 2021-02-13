from django import forms
from .models import User

class StudentRegiser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','Dob','city','password']