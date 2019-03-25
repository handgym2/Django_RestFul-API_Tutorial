from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MyclassSerializer, UsnclassSerializer
from tutorial.models import Myclass, Usnclass

from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
# Create your views here.

class MyclassViewSet(viewsets.ModelViewSet):
    queryset = Myclass.objects.all()
    serializer_class = MyclassSerializer


class UsnclassViewSet(viewsets.ModelViewSet):
    queryset = Usnclass.objects.all()
    serializer_class = UsnclassSerializer




@receiver(post_save, sender=settings.AUTH_USER_MODEL)   #User가 생성되면 자동으로 토큰을 추가해준다.
def create_auth_token(sender, instance=None, created=False, **kwargs):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)



