from django import forms
from student_manage.models import Student

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={
            'fname':'First Name',
            'lname':'Last Name',
            'email':'Email',
            'phone':'Phone No',
                        
        }
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.Select(attrs={'class': 'form-control'}),
        }