from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(label='Subject', max_length=100)
    name = forms.CharField(label='Your name', max_length=100)
    message = forms.CharField(widget=forms.Textarea)

