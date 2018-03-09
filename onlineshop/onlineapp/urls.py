from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    #url(r'^$', views.index,name='index'),
    url(r'^product/', views.product,name='product'),
    url(r'^signup/', views.signup,name='signup'),
    

    #url(r'^adminindex/', views.adminindex,name='adminindex'),
]
