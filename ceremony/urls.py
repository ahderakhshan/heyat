from django.urls import path
from .views import CreateCeremony, AddCeremonyImage, AddAudioFile,\
                    Ceremonyimage, ShowCeremony, AddCeremonyTitleImage,\
                    AllCeremony, AllNamahang, CreateNamahang, NewestNamahang,\
                    LastsCeremony, ChangeNextCeremony, ShowNextCeremony, ShowNamahang

urlpatterns = [
    path('addceremony/', CreateCeremony.as_view()),
    path('addpicture/', AddCeremonyImage.as_view()),
    path('addaudio/', AddAudioFile.as_view()),
    path('showceremony/', ShowCeremony.as_view()),
    path('addtitleimg/', AddCeremonyTitleImage().as_view()),
    path('allceremony/', AllCeremony.as_view()),
    path('allnamahang/', AllNamahang.as_view()),
    path('createnamahang/', CreateNamahang.as_view()),
    path('newestnamahang/', NewestNamahang.as_view()),
    path('lastceremonies/', LastsCeremony.as_view()),
    path('changenextceremony/', ChangeNextCeremony.as_view()),
    path('shownextceremony/', ShowNextCeremony.as_view()),
    path('shownamahang/', ShowNamahang.as_view())
]
