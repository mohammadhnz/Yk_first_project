from BaseAdvertising import BaseAdvertising as BaseAdvertising


class Ad(BaseAdvertising):

    def __init__(self, id, title, imgUrl, link, advertiser):
        super(Ad, self).__init__(id)
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_imgUrl(self):
        return self.__imgUrl

    def set_imgUrl(self, url):
        self.__imgUrl = url

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def inc_clicks(self):
        self.__advertiser.inc_clicks()
        self._clicks += 1

    def inc_views(self):
        self.__advertiser.inc_views()
        self._views += 1

    def help(self):
        pass

    def describe_me(self):
        return "this is ad class"
