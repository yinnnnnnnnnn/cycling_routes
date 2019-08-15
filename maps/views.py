import sys
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Route, RouteForm
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class HomePageView(TemplateView):
    form_class = RouteForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs): 
        form = self.form_class()
        selected_route = {}

        return render(request, self.template_name, { 'form': form, 'selected_route': selected_route })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        selected_route = {}
        if form.is_valid():
            selected_route_id = form.cleaned_data['selected_route_id']
            if selected_route_id > 0:
                selected_route = model_to_dict(Route.objects.get(id = selected_route_id))
                selected_route['audio_display'] = selected_route['audio_display'].url
                selected_route['surfaces'] = selected_route['surfaces'].split(',')

        return render(request, self.template_name, { 'form': form, 'selected_route': selected_route })
