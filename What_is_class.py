"""     Метод __call__
Лучший способ предохранения
информации о состоянии в языке Python"""


class ButtonColor:
    def __init__(self, color:str):
        self.color = color

    def __call__(self):
        return self.color
def colour(color: str):
    def inner():
        return color

    return inner

I = colour('Red')
D = colour('Blue')

cb4 = (lambda color='Yellow': 'turn ' + color)
cb5 = (lambda color='Green': 'turn ' + color)


if __name__ == '__main__':
    B = ButtonColor('Blue')
    R = ButtonColor('Red')
    print(B())
    print(R())
    print(I(), '\n', D())
    print(cb4())
    print(cb5())
