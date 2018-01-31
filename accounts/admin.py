from django.contrib import admin
from .models import reviewtable,userinfo,follow
# Register your models here.

class reviewtableadmin(admin.ModelAdmin):
	list_display=["title","description","user","date"]

class userinfoadmin(admin.ModelAdmin):
	list_display=["username","firstname","lastname","public_email","url","institution","location",'profilepic']

class followadmin(admin.ModelAdmin):
	list_display=["fromuser","touser"]


admin.site.register(reviewtable,reviewtableadmin)
admin.site.register(userinfo,userinfoadmin)
admin.site.register(follow,followadmin)