"""Замена словаря"""


class Simple: pass

dct = {}

if __name__ == '__main__':
    dct['name'] = 'Илья'
    dct['age'] = '43'
    dct['jobs'] = 'Busdriver'

    Simple.name = 'Илья'
    Simple.age = '43'
    Simple.jobs = 'Busdriver'

