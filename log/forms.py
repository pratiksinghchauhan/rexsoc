from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class loginform(AuthenticationForm):
	username=forms.CharField(label="Username",max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label="Password", max_length=30, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'})))


class signupform(forms.Form):
	username=forms.CharField(label='Username',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':'username','placeholder':'Username'}))
	email=forms.EmailField(label='Email',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':'email','placeholder':'E-mail'}))
	password1 = forms.CharField(label="Password", max_length=30, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Password'})))
	password2 = forms.CharField(label="Password(again)", max_length=30, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password(again)','placeholder':'Confirm Password'})))

	def clean_username(self):
		try:
			user=User.objects.get(username__iexact=self.cleaned_data["username"])
		except User.DoesNotExist:
			return self.cleaned_data["username"]
		raise forms.ValidationError("Username already exists.... Please try a new one!!!")

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
			return self.cleaned_data




	
