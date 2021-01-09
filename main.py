from advertising.ad import Ad as Ad
from advertising.advertiser import Advertiser as Advertiser

advertiser1 = Advertiser(1, "Ali")
advertiser2 = Advertiser(2, "Ali1")
ad1 = Ad(1, "Max", "sth", "sth", advertiser1)
ad2 = Ad(2, "Max2", "sth", "sth", advertiser2)
print(ad2.describe_me())
print(advertiser1.describe_me())
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
print(advertiser2.name)
advertiser2.name = "Noob"
print(advertiser2.name)
print(ad1.clicks)
print(advertiser2.clicks)
print(Advertiser.get_total_clicks())
print(Advertiser.help())
