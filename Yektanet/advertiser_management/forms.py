from django import forms

from .models import Advertiser


class CreateAd(forms.Form):
    pass
    advertiser_id = forms.ChoiceField(choices=Advertiser.getChoiceList(), label="AdvertiserId")
    image = forms.ImageField()
    title = forms.CharField(max_length=30, label="Title")
    link = forms.URLField(label='URL')

    def is_valid(self):

        return super().is_valid() or True
