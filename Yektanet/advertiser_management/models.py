from django.db import models
from django.utils import timezone


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

    def inc_views(self):
        self.views += 1
        self.save()

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    @staticmethod
    def getChoiceList():
        list1 = []
        for advertiser in Advertiser.objects.all():
            list1.append((advertiser.id, advertiser.name + " id: " + str(advertiser.id)))
        return list1

    @staticmethod
    def get_by_id(id):
        for advertiser in Advertiser.objects.all():
            if advertiser.id == id:
                return advertiser


class Ad(models.Model):
    APPROVE_CHOICES = (
        ('a','APPROVED'),
        ('d','Disapproved'),
        ('n','Not checked')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", default="")
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approve = models.CharField(max_length=1,choices=APPROVE_CHOICES,default=APPROVE_CHOICES[2])


    def __str__(self):
        return str(self.id)

    @classmethod
    def create(cls, title, link, image, advertiser):
        ad = cls(title=title, link=link, image=image, advertiser=advertiser)
        ad.save()
        return ad

    @staticmethod
    def inc_all_views(ip):
        for ad in Ad.objects.all():
            ad.inc_views(ip)

    def inc_views(self, ip):
        view = View.objects.create(ip=ip, ad=self)
        self.advertiser.inc_views()
        view.save()

    def inc_clicks(self, ip):
        click = Click.objects.create(ip=ip, ad=self)
        self.advertiser.inc_clicks()
        click.save()


class View(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    ip = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now())


class Click(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    ip = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now())

