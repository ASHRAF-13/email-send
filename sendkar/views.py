from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Sendemail
from .serializer import SendemailSerializer

# Create your views here.
class SendemailViewSet (ModelViewSet):
    serializer_class = SendemailSerializer
    queryset = Sendemail.objects.all()
