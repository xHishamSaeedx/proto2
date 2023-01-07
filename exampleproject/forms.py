from django.forms import ModelForm,widgets
from django import forms
from .models import *
from django.forms.fields import DateField


class ClassprojectForm(ModelForm):
    class Meta:
        model = Classproject
        fields = ['title','featured_image']

class semesterForm(ModelForm):
    class Meta:
        model = semester
        fields = ['name','curriculum','branches']

        widgets = {
            'branches': forms.CheckboxSelectMultiple(),
        }
        

class branchForm(ModelForm):
    class Meta:
        model = branch
        fields = ['name']


class subjectForm(ModelForm):
    class Meta:
        model = subject
        fields = ['name','branch','units']

        widgets = {
            'units': forms.CheckboxSelectMultiple(),
        }
        
        

class unitForm(ModelForm):
    class Meta:
        model = unit
        fields = ['name','topic','weightage']

        widgets = {
            'topic': forms.CheckboxSelectMultiple(),
        }

        
class topicForm(ModelForm):
    class Meta:
        model = topic
        fields = ['name','rating']


class timetableForm(ModelForm):
    class Meta:
        model = Timetable1
        fields = ['start_date','end_date','num_subjects','weekday_hrs','weekend_hrs']

        widgets = {
            'subjects': forms.CheckboxSelectMultiple(),
        }

class timetableForm2(ModelForm):
    class Meta:
        model = Timetable2
        fields = ['custom_date','custom_hrs']


class whatsubjectForm(ModelForm):
    class Meta:
        model = whatsubjects
        fields = ["subjects"]

class timetableForm3(ModelForm):
    class Meta:
        model = sumn
        fields = ['units']


class subjecthrsForm(ModelForm):
    class Meta:
        model = subjecthrs
        fields = ['subject_hrs','priority']

    


