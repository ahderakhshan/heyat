from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import CeremonySerializer
# Create your views here.


class CreateCeremony(CreateAPIView):
    serializer_class = CeremonySerializer
