class C1:
    x = 5
    y = 10


class C2:
    x = 1
    w = 2


class C(C1, C2):
    a = 11
    y = 12


E = C()
E1 = C1()
E2 = C2()

print(E)
print(E1)
print(E2)
