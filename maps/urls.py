from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)