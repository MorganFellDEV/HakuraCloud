"""hakuracloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from hakura.views import welcome,userdetails,allusers,createuser,createpost,logoutuser,updateprofile, followuser,debug_followers

urlpatterns = [
    path('',welcome),
    path('admin/', admin.site.urls),
    path('profiles/<id>', userdetails),
    path('allusers',allusers),
    path('createuser',createuser, name='createuser'),
    path('createpost',createpost, name='createpost'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout', logoutuser),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    path('updateprofile',updateprofile),
    path('followuser/<id>', followuser),
    path('debug_followers', debug_followers)
]
