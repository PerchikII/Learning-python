"""Первый пример"""


class First_class:
    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)


X = First_class()
Y = First_class()

X.set_data(3.14)
Y.set_data("Илья")

X.data = "Переопределение значения атрибута"

X.newname = "Ирочка" # Новый атрибут

X.display()
Y.display()
print(X.newname)
