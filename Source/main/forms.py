from django import forms
from .models import User

class StudentRegiser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['no','name','email','Dob','city','password']
        widgets ={
            'no':forms.TextInput(attrs={'class':'form-control','id':'noid'}),
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email':forms.TextInput(attrs={'class':'form-control','id':'emailid'}),
            'city':forms.TextInput(attrs={'class':'form-control','id':'cityid'}),
            'Dob':forms.TextInput(attrs={'class':'form-control','id':'dobid'}),
            'password':forms.TextInput(attrs={'class':'form-control','id':'passwordid'}),
        }