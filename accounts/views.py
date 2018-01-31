from django.shortcuts import render
from .forms import reviewform,userinfoform,picuploadform
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import reviewtable,userinfo,follow
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url="home")
def userhome(request):
	query=reviewtable.objects.all()[:1]
	queryown=reviewtable.objects.filter(user=request.user.username)[:1]
	user=User.objects.get(username=request.user.username)
	try:
		following=follow.objects.filter(fromuser=user)
		feed=list()
		for items in following:
			feed.append(reviewtable.objects.filter(user=items.touser))

	except:
		feed=""

	return render(request,"userhome.html",{'query':query,'queryown':queryown,'feed':feed})




@login_required(login_url="/login/")
def reviewview(request):
	if request.method =="POST":
		form=reviewform(request.POST)

		if form.is_valid():
			cd=form.cleaned_data
			instance=form.save(commit=True)
			instance.user=request.user.username
			instance.save()
			return HttpResponseRedirect("/submitreview/")

	form=reviewform()
	return render(request,"reviews.html",{'form':form})




@login_required(login_url="/login/")
def submitreview(request):
	return render(request,"submitreview.html")




def blog(request):
	query=reviewtable.objects.all()
	return render(request,"blog.html",{'query':query})




@login_required(login_url="/login/")
def profilesettings(request):
	if request.method =="POST":
		try:
			check=userinfo.objects.get(username=request.user.username)
		except:
			check=""
		form=userinfoform(request.POST)

		if not check:
		    if form.is_valid():
		    	cd=form.cleaned_data
		    	instance=form.save(commit=True)
		    	instance.username=request.user.username
		    	instance.save()
		    	return HttpResponseRedirect("/submitreview/")
		else:
			if form.is_valid():
				cd=form.cleaned_data
				if request.POST.get("firstname"):
				   check.firstname=request.POST.get("firstname")
				if request.POST.get("lastname"):
				   check.lastname=request.POST.get("lastname")
				if request.POST.get("public_email"):
				   check.public_email=request.POST.get("public_email")
				if request.POST.get("url"):
				   check.url=request.POST.get("url")
				if request.POST.get("institution"):
				   check.institution=request.POST.get("institution")
				if request.POST.get("location"):
				   check.location=request.POST.get("location")
				check.save()
				return HttpResponseRedirect("/submitreview/")

	form=userinfoform()
	return render(request,"profilesettingsprofile.html",{'form':form})




@login_required(login_url="/login/")
def emailsettings(request):
	user=User.objects.get(username=request.user.username)
	if request.method=="POST":
		res=request.POST.get("email")
		user.email=res
		user.save()
	return render(request,"profilesettingsemail.html",{'user':user})




@login_required(login_url="/login/")
def passwordsettings(request):
	user=User.objects.get(username=request.user.username)
	if request.method=="POST":
		user=User.objects.get(username=request.user.username)
		pwd1=request.POST.get("newpassword").strip()
		pwd2=request.POST.get("confirmnewpassword").strip()
		opwd=request.POST.get("oldpassword").strip()
		if pwd1 and pwd2 and opwd:
			if pwd1==pwd2:
				if user.check_password(opwd):
					user.set_password(pwd1)
					user.save()
					return HttpResponseRedirect("/submitreview/")
	return render(request,"profilesettingspassword.html")




@login_required(login_url="/login/")
def you(request):
	reviewfound=reviewtable.objects.filter(user=request.user.username)
	u=User.objects.get(username=request.user.username)
	followcount=follow.objects.filter(fromuser=u).count()
	followingcount=follow.objects.filter(touser=u).count()
	try:
	    query=userinfo.objects.get(username=request.user.username)
	except:
		query=" "
	return render(request,"you.html",{'query':query,'reviewfound':reviewfound,'followcount':followcount,"followingcount":followingcount})




@login_required(login_url="/login/")
def picuploadsettings(request):
	#try:		
	try:
		if request.method=="POST":
			pic=userinfo.objects.get(username=request.user.username)
			form=picuploadform(request.POST,request.FILES)
			if form.is_valid():
				pic.profilepic=request.FILES["profilepic"]
				pic.save()
				return render(request,"submitreview.html")

	except:
		if request.method=="POST":
			form=picuploadform(request.POST,request.FILES)
			if form.is_valid():
				instance=form.save(commit=True)
				instance.username=request.user.username
				instance.profilepic=request.FILES["profilepic"]
				instance.save()
				HttpResponseRedirect('/submitreview/')
	form=picuploadform()
	return render(request,"profilesettingspicture.html",{"form":form})




@login_required(login_url="/login/")
def searchresults(request):
	if request.method=="POST":
		query=User.objects.filter(username__icontains=request.POST.get("searchbox")).exclude(username=request.user.username)
		return render(request,"searchresults.html",{'query':query})
	else:
		return HttpResponseRedirect("/userhome/")



@login_required(login_url="/login/")
def someone(request,offset):
	if offset==request.user.username:
		return HttpResponseRedirect("/profile/")
 
	try:
	     query=userinfo.objects.get(username=offset)
	except:
	     query=User.objects.get(username=offset)

	reviewfound=reviewtable.objects.filter(user=offset)
	
	fr=User.objects.get(username=request.user.username)
	tr=User.objects.get(username=offset)
	wing=follow.objects.filter(fromuser=fr,touser=tr)

	if request.method=="POST":
		choice=request.POST.get("follow")
		da=follow(fromuser=fr,touser=tr)
		if choice=="follow":
			da.save()
		else:
			wing.delete()

	u=User.objects.get(username=offset)
	followcount=follow.objects.filter(touser=u).count()
	followingcount=follow.objects.filter(fromuser=u).count()

	return render(request,"someone.html",{'query':query,'wing':wing,'followcount':followcount,"followingcount":followingcount,'reviewfound':reviewfound})


	










