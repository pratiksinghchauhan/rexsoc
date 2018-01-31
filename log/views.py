from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import signupform
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


@user_passes_test(lambda u: not u.is_authenticated(),login_url="/userhome/",redirect_field_name="/userhome/")
def signup(request):
	if request.method=="POST":
		form=signupform(request.POST)
		if form.is_valid():
			user=User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
			return HttpResponseRedirect('/success/')
	return render(request,'signup.html',{'form':form})

@user_passes_test(lambda u: not u.is_authenticated(),login_url="/userhome/",redirect_field_name="/userhome/")
def home(request):
	if request.method=="POST":
		form=signupform(request.POST)
		if form.is_valid():
			user=User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
			return HttpResponseRedirect('/success/')
	form=signupform()
	return render(request,'home.html',{'form':form})

def about(request):
	return render(request,"about.html")


#@login_required(login_url="login/")


	