from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView,\
                                    UpdateAPIView
from rest_framework.views import APIView

from .serializers import CeremonySerializer, PictureSerializer, AudioSerializer\
                       , ShowCeremonySerializer, CeremonyUpdateSerializer, NamahangSerializer, NextCeremonySerializer
from rest_framework.response import Response
from .models import Ceremony, Picture, Audio, Namahang, NextCeremony
from .custom_renders import JPEGRenderer, MP3Renderer, MP4Renderer
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
        if directory=='ceremony_images':
            img = Picture.objects.filter(Q(img=f"media/{directory}/{path}")).first().img
        elif directory=='title_images':
            img = Ceremony.objects.filter(Q(title_img=f"media/{directory}/{path}")).first().title_img
        elif directory == 'nextceremony':
            img = NextCeremony.objects.filter(Q(image=f"media/{directory}/{path}")).first().image
        return Response(img, content_type='image/jpg')


class CeremonyAudio(RetrieveAPIView):
    renderer_classes = [MP3Renderer]

    def get(self,request, path):
        audio = Audio.objects.filter(Q(audio=f"audios/{path}")).first().audio
        return Response(audio, content_type='audio/mp3')


class AddCeremonyTitleImage(APIView):
    def put(self,request):
        try:
            img = request.FILES['image']
            id = request.data['id']
            instance = Ceremony.objects.get(id=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance.title_img = img
        return Response(status=status.HTTP_200_OK)


class AllCeremony(ListAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = ShowCeremonySerializer


class AllNamahang(ListAPIView):
    queryset = Namahang.objects.all()
    serializer_class = NamahangSerializer


class CreateNamahang(CreateAPIView):
    serializer_class = NamahangSerializer


class ShowNamahangVideo(RetrieveAPIView):
    renderer_classes = [MP4Renderer]

    def get(self,request, path):
        audio = Namahang.objects.filter(Q(video=f"video/{path}")).first().video
        return Response(audio, content_type='video/mp4')


class NewestNamahang(ListAPIView):
    serializer_class = NamahangSerializer

    def get_queryset(self):
        if Namahang.objects.count() < 5:
            return Namahang.objects.all()
        else:
            return Namahang.objects.order_by('-id')[:5]


class LastsCeremony(ListAPIView):
    serializer_class = ShowCeremonySerializer

    def get_queryset(self):
        if Ceremony.objects.count()<5:
            return Ceremony.objects.all()
        else:
            return Ceremony.objects.order_by('-id')[:5]


class ChangeNextCeremony(APIView):
    def post(self, request):

        if NextCeremony.objects.count() == 0:
            next_ceremony = NextCeremony()
        else:
            next_ceremony = NextCeremony.objects.first()
            next_ceremony.image.delete()
        next_ceremony.title = self.request.data['title']
        next_ceremony.about = self.request.data['about']
        next_ceremony.location = self.request.data['location']
        next_ceremony.image = self.request.FILES['image']

        next_ceremony.save()
        return Response(status=status.HTTP_200_OK)


class ShowNextCeremony(ListAPIView):
    queryset = NextCeremony.objects.all()
    serializer_class = NextCeremonySerializer


class ShowNamahang(ListAPIView):
    serializer_class = NamahangSerializer

    def get_queryset(self):
        namahang_id = self.request.query_params['namahang']
        return Namahang.objects.filter(id=namahang_id)
    