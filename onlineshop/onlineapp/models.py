from __future__ import unicode_literals

from django.db import models
#from django import forms
# Create your models here.

class category(models.Model):
   	categoryname = models.CharField(max_length = 50)

	class Meta:
		db_table = "category"


class brand(models.Model):
   	brandname = models.CharField(max_length = 50)

	class Meta:
		db_table = "brand"


class item(models.Model):
   	categoryid = models.ForeignKey(category,on_delete=models.CASCADE)
   	brandid = models.ForeignKey(brand,on_delete=models.CASCADE)
	itemname = models.CharField(max_length = 50)
	price = models.IntegerField()
	discountprice = models.IntegerField()
	description = models.TextField(max_length = 250)
	#img1 = models.CharField(max_length = 250)
	#img2 = models.CharField(max_length = 250)
	img1 = models.FileField(upload_to='uploads/')
	img2 = models.FileField(upload_to='uploads/')
	updatedate=models.DateField()   	

	class Meta:
		db_table = "item"


class users(models.Model):
	email = models.EmailField(max_length = 50)
	password = models.CharField(max_length=50)

	class Meta:
		db_table = "users"


class admin(models.Model):
	email = models.EmailField(max_length = 50)
	password = models.CharField(max_length=50)

	class Meta:
		db_table = "admin"








