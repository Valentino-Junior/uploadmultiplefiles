from django import forms


class MyfileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))