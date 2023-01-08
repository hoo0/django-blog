"""dalgona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views
from zenith import urls as zenithUrls
#import mainapp.views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('zenith/', include(zenithUrls)), # include('zenith.urls')
    
    path('login/', views.LoginView.as_view(), name='login'), # 기본템플릿: registration/login.html
    path('logout/', views.LogoutView.as_view(), name='logout'), #redirect: naext_page='/'
    
    #allauth
    path('accounts/', include('allauth.urls')),
    
    #path('google', GoogleLoginApi.as_view(), name='google_login'),
    #path('google/callback', GoogleSigninCallBackApi.as_view(), name='google_login_callback'),
]
