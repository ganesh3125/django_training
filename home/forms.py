from django import forms
from home.models import student
from django.db import models

class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'search'}))

class studenteditform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Student_name'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }

class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'student name'}))
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    department=models.CharField('Departmrnt',choices=dept,blank=True,null=True,max_length=30)