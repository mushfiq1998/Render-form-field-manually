from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Mushfiq', 
        help_text='max 70 characters can be written')
    