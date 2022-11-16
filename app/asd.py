
class Asd:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        print('Getting Value')
        return self._value

    @value.setter
    def value(self, new_value):
        print(f'Setting value: {new_value}')
        self._value = new_value

    @property
    def total(self):
        print('Dzień dobry, witam.')




a = Asd(2)
a.total
a.total = 2
# print(a.value)
# a.value = 3
# print(a.value)