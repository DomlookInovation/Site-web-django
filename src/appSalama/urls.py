from django.conf.urls.static import static
from django.urls import path
from WebSite import settings
from appSalama.views import *

app_name = 'appSalama'

urlpatterns = [
    path('', index, name="home"),
    path('apropos/', about, name="about"),
    path('infrastructure/', infrastructures, name="infrastructre"),
    path('inscription/', inscription, name="inscription"),
    path('realisation/', realisations, name="realisation"),
    path('article/', articles, name="article"),
    path('contact/', contact, name="contact"),
    path('login/', connexion, name="connexion"),
    path('option/<str:slug>', option, name="option"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)