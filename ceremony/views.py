from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import CeremonySerializer, PictureSerializer, AudioSerializer\
    , ShowCeremonySerializer
from rest_framework.response import Response
from .models import Ceremony, Picture, Audio
from .custom_renders import JPEGRenderer, MP3Renderer
from PIL import Image
from django.db.models import Q
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


class Ceremonyimage(RetrieveAPIView):
    renderer_classes = [JPEGRenderer]

    def get(self,request, directory ,path):
        img = Picture.objects.filter(Q(img=f"media/{directory}/{path}")).first().img
        return Response(img, content_type='image/jpg')


class CeremonyAudio(RetrieveAPIView):
    renderer_classes = [MP3Renderer]

    def get(self,request, path):
        audio = Audio.objects.filter(Q(audio=f"audios/{path}")).first().audio
        return Response(audio, content_type='audio/mp3')