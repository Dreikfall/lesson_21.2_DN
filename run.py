from classes.shop import Shop
from classes.store import Store
from utils import main

store = Store(печеньки=19, собачки=50, коробки=30)
shop = Shop(печеньки=0, собачки=0, коробки=0)

if __name__ == '__main__':
    main(store, shop)
