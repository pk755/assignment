from django import forms

class NumberForm(forms.Form):
    numbers = forms.CharField(label='Enter numbers (comma-separated)', required=False)
    file = forms.FileField(label='Upload file', required=False)
