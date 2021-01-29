from django import forms

from .models import Advertiser


class CreateAd(forms.Form):
    advertiser_id = forms.ChoiceField(choices=Advertiser.getChoiceList(), label="AdvertiserId")
    image = forms.ImageField(label="Image")
    title = forms.CharField(max_length=30, label="Title")
    link = forms.URLField(label='URL')
