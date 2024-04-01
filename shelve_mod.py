import shelve


with shelve.open('persondb') as f:

    print(f['Вика Иванова'])

    V = f['Вика Иванова']
    V.give_rise(25)

    f['Вика Иванова']= V
    print(f['Вика Иванова'])

