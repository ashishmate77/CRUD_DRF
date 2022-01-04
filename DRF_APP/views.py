from django.shortcuts import render
from DRF_APP.serializers import UserSerializer
from DRF_APP.models import UserReg
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = UserReg.objects.all()
    serializer_class = UserSerializer
