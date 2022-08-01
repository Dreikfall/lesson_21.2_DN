from classes.storage_base import Storage
from exceptions import NotEnoughSpaceStore


class Store(Storage):
    """ Класс склада унаследованный от абстрактного """
    def __init__(self, **items):
        self._items = items
        self._capacity = 100
        if sum(self._items.values()) > 100:
            raise NotEnoughSpaceStore(f'На {self}е недостаточно места, попобуйте что-то другое')

    def __repr__(self):
        return 'склад'

    def add(self, title_add, amount):
        if title_add in self._items and self.get_free_space() >= amount:
            self._items[title_add] = self._items[title_add] + amount
        elif title_add in self._items and self.get_free_space() < amount:
            raise NotEnoughSpaceStore

    def remove(self, title_rem, amount):
        if title_rem in self._items and self._items[title_rem] >= amount:
            self._items[title_rem] = self._items[title_rem] - amount
        elif title_rem in self._items and self._items[title_rem] < amount:
            raise NotEnoughSpaceStore

    def get_free_space(self):
        free_space = self._capacity - sum(self._items.values())
        if free_space < 0:
            return 0
        return free_space

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        sum_items = sum(self._items.values())
        return sum_items
