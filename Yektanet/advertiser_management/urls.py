from django.urls import path

from .views import *

app_name = "advertiser_management"
urlpatterns = [
    path('', AdvertiserManagement.as_view(), name='advertiser_management'),
    path('ads', ShowAds.as_view(), name='show_ads'),
    path('create_ad', CreateAdView.as_view(), name='create_ad'),
    path('create_ad2', adCreate, name='create_ad'),

    path('ad_detail', ShowAdDetails.as_view(), name='create_ad'),
    path('ads2', AdvertiserList.as_view(), name='create_ad'),

    path('<int:pk>/',
         AdRedirectView.as_view()
    , name='ad-redirect'),
]
