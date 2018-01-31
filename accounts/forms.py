from django import forms
from accounts.models import reviewtable,userinfo,follow
from django.contrib.auth.models import User


class reviewform(forms.ModelForm):
	class Meta:
		model=reviewtable
		fields=['title','description']
		widgets={ 'title': forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}), 'description' :forms.Textarea(attrs={'class': 'form-control', 'name': 'description'}) }


class userinfoform(forms.ModelForm):
	class Meta:
		model=userinfo
		fields=['firstname','lastname','public_email','url','institution','location']
		widgets={'firstname':forms.TextInput(attrs={'class': 'form-control', 'name': 'firstname'}),'lastname': forms.TextInput(attrs={'class': 'form-control', 'name': 'lastname'}),'public_email':forms.EmailInput(attrs={'class': 'form-control', 'name': 'public_email'}), 'url':forms.TextInput(attrs={'class': 'form-control', 'name': 'url'}),'institution':forms.TextInput(attrs={'class': 'form-control', 'name': 'institution'}),'location':forms.TextInput(attrs={'class': 'form-control', 'name': 'location'})}


class picuploadform(forms.ModelForm):
	class Meta:
		model=userinfo
		fields=['profilepic']
