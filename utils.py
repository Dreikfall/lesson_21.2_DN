from classes.request import Request
from exceptions import NotEnoughSpaceStore, NotEnoughSpaceShop


def statistic(obj_store, obj_shop):
    print(f'\nВ {obj_store} храниться:')
    for k, v in obj_store.get_items().items():
        print(v, k)

    print(f'\nВ {obj_shop} храниться:')
    for k, v in obj_shop.get_items().items():
        print(v, k)


def main(obj_store, obj_shop):
    statistic(obj_store, obj_shop)
    rqst = True
    while rqst:
        try:
            rqst = input('\nНапишите запрос типа: "Доставить 3 (собачки/печеньки/коробки) из склад в магазин": ')
            rqst_ = Request(rqst)
        except IndexError:
            print('Неверный формат запроса')
            continue
        if rqst_.product not in obj_store.get_items():
            print('Данного товара нет на складе')
            continue
        try:
            obj_shop.add(rqst_.product, rqst_.amount)
            obj_store.remove(rqst_.product, rqst_.amount)
        except NotEnoughSpaceShop:
            print(f'В {obj_shop}е недостаточно места попробуйте что-то другое')
            continue
        except NotEnoughSpaceStore:
            print(f'Не хватает на {obj_store}е попробуйте заказать меньше')
            obj_shop.remove(rqst_.product, rqst_.amount)
            continue
        print('\nНужное количество есть на складе')
        print(f'Курьер забрал {rqst_.amount} {rqst_.product} со {obj_store}')
        print(f'Курьер везет {rqst_.amount} {rqst_.product} со {obj_store} в {obj_shop}')
        print(f'Курьер доставил {rqst_.amount} {rqst_.product} в {obj_shop}')
        statistic(obj_store, obj_shop)

