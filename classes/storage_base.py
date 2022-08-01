from abc import ABC, abstractmethod


class Storage(ABC):
    """ Абстрактный класс """

    @abstractmethod
    def add(self, title_add, amount):
        pass

    @abstractmethod
    def remove(self, title_rem, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

