from abc import abstractmethod, ABC


class BaseAdvertising(ABC):

    def __init__(self, id):
        self.__id = id
        self._clicks = 0
        self._views = 0

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

    def describe_me(self):
        return "common parent of ad and advertiser"

    @abstractmethod
    def describe_me(self):
        pass
