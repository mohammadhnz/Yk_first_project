from django.urls import path
from . import views
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from .models import Ad

app_name = "advertiser_management"
urlpatterns = [
    path('', views.advertiser_management1, name='advertiser_management'),
    path('ads', views.show_ads, name='show_message'),
    path('create_ad', views.create_ad, name='create_ad'),
    path('<int:pk>/',
         views.AdRedirectView.as_view()
    , name='ad-redirect'),
]
