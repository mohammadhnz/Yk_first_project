from django.http import HttpResponse
from django.shortcuts import render

from .models import Advertiser, Ad


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


def show_message(request):
    class advertiser_proxy:
        def __init__(self, name, id, clicks, views, ads):
            self.name = name
            self.id = id
            self.clicks = clicks
            self.views = views
            self.ads = ads

    advertisers = []
    for advertiser in Advertiser.objects.all():
        list_of_ads = inc_views(advertiser)
        advertisers.append(
            advertiser_proxy(advertiser.name, advertiser.id, advertiser.clicks, advertiser.views, list_of_ads))
    context = {
        "advertisers": advertisers,
    }
    return render(request, "advertiser_management/ads.html", context)


def inc_views(advertiser):
    list_of_ads = Ad.objects.filter(advertiser_id=advertiser.id)
    for ad in list_of_ads:
        ad.views  = ad.views + 1
    advertiser.views += len(list_of_ads)
    return list_of_ads
