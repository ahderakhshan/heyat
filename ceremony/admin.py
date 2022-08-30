from django.contrib import admin
from .models import Ceremony, Picture, Audio, Namahang, NextCeremony
# Register your models here.
admin.site.register(Ceremony)
admin.site.register(Picture)
admin.site.register(Audio)
admin.site.register(Namahang)
admin.site.register(NextCeremony)