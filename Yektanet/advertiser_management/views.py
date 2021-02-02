from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import RedirectView

from .forms import CreateAd
from .models import Advertiser, Ad


class AdRedirectView(RedirectView):
    pattern_name = 'ad-redirect'
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.inc_clicks()
        return ad.link


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


def create_ad(request):
    if request.method == 'POST':
        form = CreateAd(request.POST, request.FILES)
        if form.is_valid():
            advertiser_id1 = form.cleaned_data.get('advertiser_id')
            image1 = form.cleaned_data.get('image')
            title1 = form.cleaned_data.get('title')
            link1 = form.cleaned_data.get('link')
            Ad.create(title1, link1, image1, Advertiser.objects.get(pk=int(advertiser_id1)))
            return HttpResponseRedirect('ads')
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
    Ad.inc_all_views()
    for advertiser in Advertiser.objects.all():
        list_of_ads = Ad.objects.filter(advertiser_id=advertiser.id)
        advertisers.append(
            advertiser_proxy(advertiser.name, advertiser.id, advertiser.clicks, advertiser.views, list_of_ads))
    context = {
        "advertisers": advertisers,
    }
    return render(request, "advertiser_management/ads.html", context)
