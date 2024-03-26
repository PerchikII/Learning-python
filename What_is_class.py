"""Замена словаря"""


class Simple: pass



if __name__ == '__main__':
    persona_1 = Simple()
    persona_1.name = 'Илья'
    persona_1.age = '43'
    persona_1.jobs = 'Busdriver'

    persona_2 = Simple()
    persona_2.name = 'Вика'
    persona_2.age = '41'
    persona_2.jobs = 'Teacher'

    print(persona_1.jobs)
    print(persona_2.jobs)




