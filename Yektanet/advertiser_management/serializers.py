from rest_framework import serializers

from .models import Ad, Advertiser, View, Click
from datetime import datetime


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailedSerializer(serializers.ModelSerializer):
    clicks_per_hour = serializers.SerializerMethodField()
    views_per_hour = serializers.SerializerMethodField()
    click_rate = serializers.SerializerMethodField()
    average_click_time = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = '__all__'

    def get_clicks_per_hour(self, instance):
        clicks_per_hour = self.get_click_per_hour(instance)
        clicks_per_hour = list(
            str(i) + " - " + str(i + 1) + ": " + str(x) for i, x in enumerate(clicks_per_hour))
        return clicks_per_hour

    def get_click_per_hour(self, instance):
        clicks_per_hour = list(len(Click.objects.filter(ad_id=instance.id,
                                                        date__gt=datetime.now().replace(hour=x,
                                                                                        minute=0,
                                                                                        second=0,
                                                                                        microsecond=0)
                                                        , date__lt=datetime.now().replace(hour=x + 1,
                                                                                          minute=0,
                                                                                          second=0,
                                                                                          microsecond=0)))
                               for x in
                               range(23))
        return clicks_per_hour

    def get_views_per_hour(self, instance):
        views_per_hour = self.get_view_per_hour(instance)
        views_per_hour = list(
            str(i) + " - " + str(i + 1) + ": " + str(x) for i, x in enumerate(views_per_hour))
        return views_per_hour

    def get_view_per_hour(self, instance):
        views_per_hour = list(len(View.objects.filter(ad_id=instance.id,
                                                      date__gt=datetime.now().replace(hour=x,
                                                                                      minute=0,
                                                                                      second=0,
                                                                                      microsecond=0)
                                                      , date__lt=datetime.now().replace(hour=x + 1,
                                                                                        minute=0,
                                                                                        second=0,
                                                                                        microsecond=0)))
                              for x in
                              range(23))
        return views_per_hour

    def get_click_rate(self, instance):
        views_per_hour = self.get_view_per_hour(instance)
        clicks_per_hour = self.get_click_per_hour(instance)
        click_rate = list(((clicks_per_hour[i] / views_per_hour[i]) if views_per_hour[
                                                                           i] != 0 else 0) for i
                          in range(23))
        click_rate = list(
            str(i) + " - " + str(i + 1) + ": " + str(x) for i, x in enumerate(click_rate))
        return click_rate

    def get_average_click_time(self, instance):
        ip_dict1 = list(View.objects.filter(ad_id=instance.id).values('ip'))
        ip_dict2 = list(Click.objects.filter(ad_id=instance.id).values('ip'))
        ip_set1, ip_set2 = set(), set()
        for ip in ip_dict1:
            ip_set1.add(ip['ip'])
        for ip in ip_dict2:
            ip_set2.add(ip['ip'])
        sum = 0
        if ip_set2 & ip_set1:
            for ip in ip_set1 & ip_set2:
                sum += (View.objects.get(ip=ip, ad_id=instance.id).date - Click.objects.get(ip=ip,
                                                                                                     ad_id=instance.id).date).total_seconds()
            sum /= len(ip_set2 & ip_set1)
        return str(sum)


class AdvertiserSerializer(serializers.ModelSerializer):
    ads = serializers.SerializerMethodField()

    class Meta:
        model = Advertiser
        fields = '__all__'

    def get_ads(self, instance):
        return AdSerializer(Ad.objects.filter(advertiser_id=instance.id), many=True).data


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'
