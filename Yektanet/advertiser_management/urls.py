from django.urls import path

from .views import *

app_name = "advertiser_management"
urlpatterns = [
    path('', AdvertiserManagement.as_view(), name='advertiser_management'),
    path('ads', ShowAds.as_view(), name='show_ads'),
    path('create_ad', AdCreate.as_view(), name='create_ad'),
    path('ad_detail', AdDetailedList.as_view(), name='create_ad'),
    path('ads2', AdList.as_view(), name='create_ad'),

    path('<int:pk>/',
         AdRedirectView.as_view()
    , name='ad-redirect'),
]
