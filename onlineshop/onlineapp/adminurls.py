from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    #url(r'^$', views.index,name='index'),
    #url(r'^product/', views.product,name='product'),
    #url(r'^signup/', views.signup,name='signup'),
    url(r'^adminindex/', views.adminindex,name='adminindex'),
    
    url(r'^brandentry/', views.brandentry,name='brandentry'),
    url(r'^brandupdate', views.brandupdate,name='brandupdate'),
    url(r'^savebrand/', views.savebrand,name='savebrand'),
    url(r'^updatebrand/', views.updatebrand,name='updatebrand'),
    url(r'^deletebrand', views.deletebrand,name='deletebrand'),
    url(r'^brandlist/', views.brandlist,name='brandlist'),
    
    url(r'^categoryentry/', views.categoryentry,name='categoryentry'),
    url(r'^categoryupdate', views.categoryupdate,name='categoryupdate'),
    url(r'^savecategory/', views.savecategory,name='savecategory'),
    url(r'^updatecategory/', views.updatecategory,name='updatecategory'),
    url(r'^deletecategory', views.deletecategory,name='deletecategory'),
    url(r'^categorylist/', views.categorylist,name='categorylist'),
    
    url(r'^itementry/', views.itementry,name='itementry'),
    url(r'^saveitem/', views.saveitem,name='saveitem'),
    url(r'^itemlist/', views.itemlist,name='itemlist'),
    
    
    

]
