from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer 
from .models import Sendemail

class SendemailSerializer (ModelSerializer):
    class Meta:
        model= Sendemail
        fields = '__all__'