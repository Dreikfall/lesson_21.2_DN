from classes.store import Store
from exceptions import NotEnoughSpaceShop


class Shop(Store):
    """ Класс магазина унаследованный от склада """
    def __init__(self, **items):
        super().__init__(**items)
        self._capacity = 20
        if sum(self._items.values()) > 20:
            raise NotEnoughSpaceShop

    def __repr__(self):
        return 'магазин'

    def add(self, title_add, amount):
        if title_add in self._items and self.get_free_space() >= amount:
            self._items[title_add] = self._items[title_add] + amount
        elif title_add in self._items and self.get_free_space() < amount:
            raise NotEnoughSpaceShop

    def remove(self, title_rem, amount):
        if title_rem in self._items and self._items[title_rem] >= amount:
            self._items[title_rem] = self._items[title_rem] - amount
        elif title_rem in self._items and self._items[title_rem] < amount:
            raise NotEnoughSpaceShop
