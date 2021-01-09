from abc import abstractmethod, ABC


class BaseAdvertising(ABC):

    def __init__(self, id):
        self._id = id
        self._clicks = 0
        self._views = 0

    @property
    def clicks(self):
        return self._clicks

    @clicks.setter
    def clicks(self, value):
        self._clicks = value

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        self._views = value

    @abstractmethod
    def describe_me(self):
        pass

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1
