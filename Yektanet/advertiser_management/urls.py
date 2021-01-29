from django.urls import path
from . import views

app_name = "advertiser_management"
urlpatterns = [
    path('', views.advertiser_management1, name='advertiser_management'),
    path('message', views.show_message, name='show_message'),
]
