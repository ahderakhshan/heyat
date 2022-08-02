from rest_framework import serializers
from .models import Ceremony, Picture, Audio


class CeremonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = '__all__'


class CeremonyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'title_img')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class ShowCeremonySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    audios = serializers.SerializerMethodField()

    class Meta:
        model = Ceremony
        fields = '__all__'

    def get_images(self, ceremony):
        return ceremony.picture_set.values_list('img')

    def get_audios(self, ceremony):
        return ceremony.audio_set.values_list('audio')