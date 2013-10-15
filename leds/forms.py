from django import forms

class ledsOnOff(forms.Form):
	estado = forms.CharField(widget=forms.TextInput)