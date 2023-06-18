"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('reg',views.reg,name='reg'),
    path('pro/<int:name>',views.pro,name='pro'),
     path('pd/<int:id>',views.pd,name='pd'),
     path('log',views.log,name='log'),
     path('logout',views.Logout,name='logout'),
      path('catagories',views.cat,name='cat'),
     path("cart/<int:id>",views.cart,name="cart"),
      path("allcart",views.allcart,name="allcart"),
      path('delcart/<int:id>',views.delcart,name='delcart'),
    

     
    
   
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)