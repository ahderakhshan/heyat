from django.urls import path
from .views import CreateCeremony, AddCeremonyImage, AddAudioFile,\
                    Ceremonyimage, ShowCeremony, AddCeremonyTitleImage,\
                    AllCeremony, AllNamahang, CreateNamahang

urlpatterns = [
    path('addceremony/', CreateCeremony.as_view()),
    path('addpicture/', AddCeremonyImage.as_view()),
    path('addaudio/', AddAudioFile.as_view()),
    path('showceremony/', ShowCeremony.as_view()),
    path('addtitleimg/', AddCeremonyTitleImage().as_view()),
    path('allceremony/', AllCeremony.as_view()),
    path('allnamahang/', AllNamahang.as_view()),
    path('createnamahang/', CreateNamahang.as_view()),
]
