from django import forms

class wordle(forms.Form):
    guess = forms.CharField(min_length=5, max_length=5, widget= forms.TextInput(attrs={"class" : 'form-control'}), required = True)