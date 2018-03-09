from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import brand
from models import category
from models import item
from django.shortcuts import redirect
import datetime

# Create your views here.

def index(request):
	username='a'
	if 'uname' in request.session:
		username=request.session['uname']	

	items=item.objects.all().order_by('id').reverse()[:6]

	template=loader.get_template('onlineapp/template/template.html')
	context={'username':username,'items':items}
	return HttpResponse(template.render(context,request))

def product(request):
	template=loader.get_template('onlineapp/template/template2.html')
	context={}
	return HttpResponse(template.render(context,request))

def signup(request):
	template=loader.get_template('onlineapp/template/signup.html')
	context={}
	return HttpResponse(template.render(context,request))	

def adminindex(request):
	template=loader.get_template('onlineapp/template/adminindex.html')
	context={}
	return HttpResponse(template.render(context,request))

def brandentry(request):
	template=loader.get_template('onlineapp/template/brandentry.html')
	context={}
	return HttpResponse(template.render(context,request))

def brandupdate(request):
	if request.method == "GET":
		brandid1=request.GET.get('id')
	 	brands=brand.objects.all().filter(id=brandid1)
	 	context={"brands":brands}
	 	template=loader.get_template('onlineapp/template/brandupdate.html')
		return HttpResponse(template.render(context,request))
	
	template=loader.get_template('onlineapp/template/brandlist.html')
	context={}
	return HttpResponse(template.render(context,request))

def brandlist(request):
	brands=brand.objects.all()

	template=loader.get_template('onlineapp/template/brandlist.html')
	context={"brands":brands}
	return HttpResponse(template.render(context,request))

def categoryentry(request):
	template=loader.get_template('onlineapp/template/categoryentry.html')
	context={}
	return HttpResponse(template.render(context,request))

def categorylist(request):
	categories=category.objects.all()

	template=loader.get_template('onlineapp/template/categorylist.html')
	context={"categories":categories}
	return HttpResponse(template.render(context,request))

def itementry(request):
	brands=brand.objects.all()
	categories=category.objects.all()
	template=loader.get_template('onlineapp/template/itementry.html')
	context={"brands":brands,"categories":categories}
	return HttpResponse(template.render(context,request))

def itemlist(request):
	template=loader.get_template('onlineapp/template/itemlist.html')
	context={}
	return HttpResponse(template.render(context,request))


def savebrand(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/brandentry.html')
 	if request.method == "POST":
 		#print("bbbbbbbbbb")
	 	brandname1=request.POST.get('brand')
 		brandinsert=brand(brandname=brandname1)
		brandinsert.save()
		return redirect('brandlist')

 	return HttpResponse(template.render(context,request))

def categoryupdate(request):
	if request.method == "GET":
		categoryid1=request.GET.get('id')
	 	categories=category.objects.all().filter(id=categoryid1)
	 	context={"categories":categories}
	 	template=loader.get_template('onlineapp/template/categoryupdate.html')
		return HttpResponse(template.render(context,request))
	
	template=loader.get_template('onlineapp/template/categorylist.html')
	context={}
	return HttpResponse(template.render(context,request))


def updatebrand(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/brandentry.html')
 	if request.method == "POST":
 		brandid1=request.POST.get('id')
	 	brandname1=request.POST.get('brand')
 		brandupdate=brand(brandname=brandname1,id=brandid1)
		brandupdate.save()
		return redirect('brandlist')

 	return HttpResponse(template.render(context,request))	

def updatecategory(request):
	context={}
 	template=loader.get_template('onlineapp/template/categoryentry.html')
 	if request.method == "POST":
 		categoryid1=request.POST.get('id')
	 	categoryname1=request.POST.get('category')
 		categoryupdate=category(categoryname=categoryname1,id=categoryid1)
		categoryupdate.save()
		return redirect('categorylist')

 	return HttpResponse(template.render(context,request))

def deletebrand(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/brandlist.html')
 	if request.method == "GET":
 		brandid1=request.GET.get('id')
 		branddelete=brand(id=brandid1)
		branddelete.delete()
		return redirect('brandlist')

 	return HttpResponse(template.render(context,request))

def deletecategory(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/categorylist.html')
 	if request.method == "GET":
 		categoryid1=request.GET.get('id')
 		categorydelete=category(id=categoryid1)
		categorydelete.delete()
		return redirect('categorylist')

 	return HttpResponse(template.render(context,request))

def savecategory(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/categoryentry.html')
 	if request.method == "POST":
 		#print("bbbbbbbbbb")
	 	category1=request.POST.get('category')
 		categoryinsert=category(categoryname=category1)
		categoryinsert.save()
		return redirect('categorylist')

 	return HttpResponse(template.render(context,request))

def saveitem(request):
	context={}
	#print("aaaaaaaa")
 	template=loader.get_template('onlineapp/template/itementry.html')
 	if request.method == "POST":
 		#print("bbbbbbbbbb")
	 	itemname1=request.POST.get('itemname')
	 	category1=int(request.POST.get('category'))
	 	brand1=int(request.POST.get('brand'))
	 	price1=request.POST.get('price')
	 	description1=request.POST.get('description')
	 	discountprice1=0;
	 	today=datetime.datetime.now().date()
	 	#img11=request.POST.get('img1')
	 	#img21=request.POST.get('img2')
	 	img11=request.FILES['img1']
	 	img21=request.FILES['img2']

 		iteminsert=item(itemname=itemname1,categoryid_id=category1,brandid_id=brand1,price=price1
 			,discountprice=discountprice1,description=description1,img1=img11,img2=img21,updatedate=today)
		iteminsert.save()
		return redirect('itemlist')

 	return HttpResponse(template.render(context,request))