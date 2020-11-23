from django.shortcuts import render
from django.http import HttpResponse
from BlogPost.models import user_details,Post 
# Create your views here.

def lo(request):
	return render(request,'index.html')
username1=''
def user(request):
	if request.method=="POST":
		global username1
		username1=request.POST["Username"]
		first_name=request.POST["first_name"]
		last_name=request.POST["last_name"]
		email=request.POST["email"]
		phone=request.POST["phone"]
		passw=request.POST["password"]
		fb=request.POST['fb']
		insta=request.POST["insta"]
		passwordConfirm=request.POST["passwordConfirm"]
		if (passw!=passwordConfirm):
			return render(request,'register.html')
		#print(user_details_login.objects.all())
		try:
			u=user_details.objects.get(username=username1)
		except:
			u=None
		if(u):
			return render(request,'register.html')
		else:
			tb=user_details()
			tb.username=username1
			tb.first_name=first_name
			tb.last_name=last_name
			tb.email=email
			tb.phone=phone
			tb.insta=insta
			tb.fb=fb
			tb.passw=passw
			tb.cpass=passwordConfirm
			tb.save()
			#print (tb.id)
			"""lo=login()
			lo.username=username1
			lo.password=passw
			lo.save()"""



		return render(request,'index.html')
	else:
		return render(request,'register.html')
'''
user_name=0
def login(request):
	if request.method=="POST":
		global username1
		p=Post.objects.all()
		username2=request.POST["user"]
		username2 = username2.strip()
		password1=request.POST["password"]
		u = user_details.objects.filter(username=username2)
		print(u.values("passw"))
		user_name=username2
		for i in u.values("passw"):
			if i["passw"] == password1:
				print("here")
				print(username2)
				username1=username2
				return render(request,'homepage1.html',{'p':p})
		return render(request,'login.html')
	else:
		return render(request,'login.html')
'''