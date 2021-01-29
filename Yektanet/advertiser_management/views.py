from django.http import HttpResponse, Http404
from django.shortcuts import render

from .forms import CreateAd
from .models import Advertiser, Ad


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


def create_ad(request):
    if request.method == 'POST':
        form = CreateAd(request.POST)
        if form.is_valid():
            advertiser_id1 = form.cleaned_data['advertiser_id']
            image1 = form.cleaned_data['image']
            title1 = form.cleaned_data['title']
            link1 = form.cleaned_data['link']
            Ad.objects.create(title=title1, link=link1, image=image1,
                                  advertiser_id=advertiser_id1)
        else:
            raise Http404("bad")
    form = CreateAd()
    return render(request, "advertiser_management/create_ad.html", {'form': form})


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
        ad.views = ad.views + 1
    advertiser.views += len(list_of_ads)
    return list_of_ads
