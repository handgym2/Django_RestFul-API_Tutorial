"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from rest_framework import routers, authtoken
from tutorial import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token #새로고침
from rest_framework_jwt.views import verify_jwt_token #확인

router = routers.DefaultRouter()
router.register('persons', views.MyclassViewSet)
router.register('ban', views.UsnclassViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api-token-auth/', obtain_jwt_token), 
    path('api-token-refresh/',refresh_jwt_token),#새로고침
    path('api-token-verify/',verify_jwt_token), #확인
    path('rest-auth/', include('rest_auth.urls')), #로그인, 로그아웃 등
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
