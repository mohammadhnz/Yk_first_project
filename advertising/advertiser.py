from advertising.base_advertising import BaseAdvertising as BaseAdvertising


class Advertiser(BaseAdvertising):
    _all_advertisers = []

    def __init__(self, id, name):
        super(Advertiser, self).__init__(id)
        self._name = name
        Advertiser._all_advertisers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @staticmethod
    def help():
        return "id: each advertiser has its own Id" \
               "\nname: name of advertiser\nclicks: count of clicks\nviews: count of views"

    def describe_me(self):
        return "this is advertiser class"

    @staticmethod
    def get_total_clicks():
        clicks = 0
        for advertiser in Advertiser._all_advertisers:
            clicks += advertiser.clicks
        return clicks
