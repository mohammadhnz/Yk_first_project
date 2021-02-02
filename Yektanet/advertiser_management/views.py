from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import RedirectView, TemplateView

from .forms import CreateAd
from .models import Advertiser, Ad


class AdRedirectView(RedirectView):
    pattern_name = 'ad-redirect'
    query_string = False
    ad = ""

    def get_redirect_url(self, *args, **kwargs):
        self.ad = get_object_or_404(Ad, pk=kwargs['pk'])
        return self.ad.link

    def get(self, request, *args, **kwargs):
        self.ad = get_object_or_404(Ad, pk=kwargs['pk'])
        self.ad.inc_clicks(request.ip)
        return super().get(request, *args, **kwargs)


def advertiser_management1(request):
    return HttpResponse("Thie is advertiser_management")


class AdvertiserManagement(TemplateView):
    template_name = "advertiser_management/advertiser_management.html"

    def get_context_data(self, **kwargs):
        context = {
            "welcome": "hello this is advertiser management view!!!", }
        return context


class CreateAdView(View):
    form_class = CreateAd
    initial = {'key': 'value'}
    template_name = 'advertiser_management/create_ad.html'

    def get(self, request, *args, **kwargs):
        form = CreateAd
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            advertiser_id1 = form.cleaned_data.get('advertiser_id')
            image1 = form.cleaned_data.get('image')
            title1 = form.cleaned_data.get('title')
            link1 = form.cleaned_data.get('link')
            Ad.create(title1, link1, image1, Advertiser.objects.get(pk=int(advertiser_id1)))
            return HttpResponseRedirect('ads')

        return render(request, self.template_name, {'form': form})


class ShowAds(TemplateView):
    template_name = "advertiser_management/ads.html"

    def get_context_data(self, **kwargs):
        class advertiser_proxy:
            def __init__(self, name, id, clicks, views, ads):
                self.name = name
                self.id = id
                self.clicks = clicks
                self.views = views
                self.ads = ads

        advertisers = []
        for advertiser in Advertiser.objects.all():
            list_of_ads = Ad.objects.filter(advertiser_id=advertiser.id, approve='a')
            advertisers.append(
                advertiser_proxy(advertiser.name, advertiser.id, advertiser.clicks, advertiser.views, list_of_ads))
        context = {
            "advertisers": advertisers,
        }
        return context

    def get(self, request, *args, **kwargs):
        Ad.inc_all_views(request.ip)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
