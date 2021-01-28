from django.db import models


# Create your models here.
class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)


class Ad(BaseAdvertising):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
