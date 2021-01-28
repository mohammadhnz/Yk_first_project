from django.db import models


# Create your models here.
class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default= 0)
    views = models.IntegerField(default= 0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=20)

class Ad(BaseAdvertising):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=100)
