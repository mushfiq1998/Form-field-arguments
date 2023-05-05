from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your name', label_suffix=' ',
    required=False, disabled=True, help_text='max 70 characters', 
    initial='Mushfiq')

