"""Наследование
отношения -'является' """

class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    def giveRise(self,percent):
        self.salary = ((self.salary / 100) * percent)+ self.salary
    def work(self):
        print(self.name,f'Делает что-то')
    def __repr__(self):
        return f'Employee:\n \tимя работника: {self.name}\n\t\tзарплата:  {self.salary}'

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)
    def work(self):
        print(self.name,f'Готовит еду')


class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,1500)
    def work(self):
        print(self.name,f'Носит еду')

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name,f'Робот готовит пиццу')

if __name__ == '__main__':

    BOB = PizzaRobot('Bob')
    print(BOB)
    for klas in Employee,Chef,Server,PizzaRobot:

        obj = klas(klas.__name__)
        obj.work()

