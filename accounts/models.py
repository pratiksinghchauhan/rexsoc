from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User


# Create your models here.

class reviewtable(models.Model):
	user=models.CharField(max_length=30)
	title=models.CharField(max_length=50)
	description=models.CharField(max_length=500)
	date=models.DateField(auto_now=True)
	class Meta:
		ordering= ['-date']

class userinfo(models.Model):
	username=models.CharField(max_length=30,null=True,default="")
	firstname=models.CharField(max_length=30,null=True,default="")
	lastname=models.CharField(max_length=30,null=True,default="")
	public_email=models.EmailField(max_length=30,null=True,default="")
	url=models.TextField(validators=[URLValidator()],null=True,default="")
	institution=models.CharField(max_length=30,null=True,default="")
	location=models.CharField(max_length=30,null=True,default="")
	profilepic=models.ImageField(default="http://www.sbesports.com/uploads/7/8/6/7/7867102/no-image_5_orig.png")

class follow(models.Model):
	fromuser=models.ForeignKey(User,related_name="follower")
	touser=models.ForeignKey(User,related_name="getsfollowed")

