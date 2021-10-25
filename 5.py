class Bill(object):
    name = "Electricity"

    @classmethod
    def display(cls):
        print(cls.name)


class Electricity(Bill):
    name = "Bill_Electricity"

    @classmethod
    def display(cls):
        print(cls.name + Bill.name)


class Gas(Bill):
    name = "Gas Bill"

    @classmethod
    def display(cls):
        print(cls.name + Bill.name)


b = Electricity()
c = Gas()
b.display()
c.display()
