from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import CeremonySerializer, PictureSerializer, AudioSerializer\
    , ShowCeremonySerializer
from .models import Ceremony
# Create your views here.


class CreateCeremony(CreateAPIView):
    serializer_class = CeremonySerializer


class AddCeremonyImage(CreateAPIView):
    serializer_class = PictureSerializer


class AddAudioFile(CreateAPIView):
    serializer_class = AudioSerializer


class ShowCeremony(ListAPIView):
    serializer_class = ShowCeremonySerializer

    def get_queryset(self):
        ceremony_id = self.request.query_params['ceremony']
        return Ceremony.objects.filter(id=ceremony_id)
