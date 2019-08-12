from django.apps import AppConfig
import os

class MapsConfig(AppConfig):
    name = 'maps'

def get_upload_path(instance, filename):
    return os.path.join('audio_display', '%d' % instance.id, filename)
