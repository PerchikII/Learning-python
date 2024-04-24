class Listinstance:
    """Подмешиваемый класс, который предоставляет форматированную функцию
print() или str () для экземпляров через наследование реализованного
в нем метода __str__ ; отображает только атрибуты экземпляра; self
является экземпляром самого нижнего класса;
имена __X предотвращают конфликты с атрибутами клиента"""
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\t{attr}={self.__dict__[attr]}\n'
        return result
    def __str__ (self) :
        return (f'Instance of {self.__class__.__name__}\n'
                f'address {id(self)}:\n'
                f'атрибуты:\n {self.__attrnames()}')


