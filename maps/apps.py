from django.apps import AppConfig
import os

class MapsConfig(AppConfig):
    name = 'maps'

def get_audio_upload_path(instance, filename):
    return os.path.join('audio_display', '%d' % instance.id, filename)

def get_elevation_upload_path(instance, filename):
    return os.path.join('elevation_profile', '%d' % instance.id, filename)
