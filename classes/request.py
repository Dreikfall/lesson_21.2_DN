class Request:
    def __init__(self, rqst: 'Доставить 3 печеньки из склад в магазин'):
        self.__from_ = rqst.split()[4]
        self.__to = rqst.split()[-1]
        self.__amount = int(rqst.split()[1])
        self.__product = rqst.split()[2]

    @property
    def from_(self):
        return self.__from_

    @property
    def to(self):
        return self.__to

    @property
    def amount(self):
        return self.__amount

    @property
    def product(self):
        return self.__product









