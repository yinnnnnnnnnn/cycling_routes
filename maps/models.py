from django import forms
from django.db import models
from django.core.validators import MinValueValidator, validate_comma_separated_integer_list
import os
import sys
from .apps import get_audio_upload_path, get_elevation_upload_path

# Create your models here.
class Route(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    lat_start = models.DecimalField(max_digits=20, decimal_places=17)
    lng_start = models.DecimalField(max_digits=20, decimal_places=17)
    lat_end = models.DecimalField(max_digits=20, decimal_places=17)
    lng_end = models.DecimalField(max_digits=20, decimal_places=17)
    audio_display = models.FileField(upload_to=get_audio_upload_path, null=True)
    surfaces = models.CharField(max_length=256, null=True, blank=True, validators=[validate_comma_separated_integer_list])
    calories = models.IntegerField(null=True)
    elevation_profile = models.ImageField(upload_to=get_elevation_upload_path, null=True)
    bike_shops= models.CharField(max_length=256, null=True, blank=True)

    @property
    def surfaces_array(self):
        return self.surfaces.split(',')

    def __str__(self):
        return self.title

def get_route_choices():
    return [(0, ' ---- Select a route ---- ')] + [(route.id, route.title) for route in Route.objects.all()]

class RouteForm(forms.Form): 
    selected_route_id = forms.IntegerField(label='Select a route', widget=forms.Select(choices=get_route_choices(), attrs={'class': 'form-control'}))


