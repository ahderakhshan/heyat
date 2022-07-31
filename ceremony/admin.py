from django.contrib import admin
from .models import Ceremony, Picture, Audio
# Register your models here.
admin.site.register(Ceremony)
admin.site.register(Picture)
admin.site.register(Audio)