"""     Метод __call__
Лучший способ предохранения
информации о состоянии в языке Python"""


class ButtonColor:
    def __init__(self, color:str):
        self.color = color

    def __call__(self):
        return self.color


if __name__ == '__main__':
    B = ButtonColor('Blue')
    R = ButtonColor('Red')
    print(B())
    print(R())
