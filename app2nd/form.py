from django import forms
from .models import UserDetails
class DataForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields ="__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control',"style" : "border: 1px solid black; "}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'pincode' : forms.TextInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            
        }