from django.urls import path

from . import views

app_name = "advertiser_management"
urlpatterns = [
    path('', views.AdvertiserManagement.as_view(), name='advertiser_management'),
    path('ads', views.ShowAds.as_view(), name='show_ads'),
    path('create_ad', views.CreateAdView.as_view(), name='create_ad'),
    path('ad_detail', views.ShowAdDetails.as_view(), name='create_ad'),

    path('<int:pk>/',
         views.AdRedirectView.as_view()
    , name='ad-redirect'),
]
