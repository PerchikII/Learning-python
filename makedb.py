import shelve
from What_is_class import Person, Manager

Ilya = Person('Илья')
Vika = Person('Вика Иванова', job='Бухгалтер',pay=100000)
Ira = Manager('Ира Иванова', pay=50000)

db = shelve.open('persondb')
for obj in (Ilya, Vika, Ira):
    db[obj.name] = obj
db.close()

