from django import forms
from .models import User

# Create your forms here.

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'enrollment', 'password', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'First & Last name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'abc123@gmail.com'}),
            'enrollment': forms.TextInput(attrs={'class':'form-control','placeholder':'0000CS000F00'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control','placeholder':'Abc@123##'}),
            'date': forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
        }