"""Объектно-ориентированное программирование
и композиция: отношения "имеет"""


import PizzaRobot as PR

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "orders from")

    def pay(self, server):
        print(self.name,"pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")


class PizzaShop:
    def __init__(self):
        self.server = PR.Server('Pat')
        self.chef = PR.PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == "__main__":
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')