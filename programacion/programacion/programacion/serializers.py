from dataclasses import field
from rest_framework import serializers
from .models import *


class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        exclude = ['id','estado']