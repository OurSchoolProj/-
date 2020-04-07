class MyZeroDivisionError(ZeroDivisionError):
    pass


class Calculator:
    def __init__(self, a, b):
        if b == 0:
            raise MyZeroDivisionError
        else:
            self.value = a / b
            self.a = a
            self.b = b
            self.command_list = ['дробь', '=']

    def __add__(self, other):
        t = Calculator(0, 1)
        if isinstance(other, int):
            t.value = self.value + other
            t.b = self.b
            t.a = self.a + self.b * other
        elif isinstance(other, Calculator):
            t.value = self.value + other.value
            t.a = self.a * other.b + self.b * other.a
            t.b = self.b * other.b
        return t

    def __radd__(self, other):
        return other + self

    def __mul__(self, other):
        t = Calculator(0, 1)
        if isinstance(other, int):
            t.value = self.value * other
            t.b = self.b
            t.a = self.a * other
        elif isinstance(other, Calculator):
            t.value = self.value * other.value
            t.a = self.a * other.a
            t.b = self.b * other.b
        return t

    def __rmul__(self, other):
        t = Calculator(0, 1)
        if isinstance(other, int):
            t.value = self.value * other
            t.b = self.b
            t.a = self.a * other
        elif isinstance(other, Calculator):
            t.value = self.value * other.value
            t.a = self.a * other.a
            t.b = self.b * other.b
        return t

    def __sub__(self, other):
        return self + (-1) * other

    def __truediv__(self, other):
        t = Calculator(0, 1)
        if isinstance(other, int):
            t.a = self.a
            t.b = self.b * other
            t.value = t.a / t.b
        elif isinstance(other, Calculator):
            t.a = self.a * other.b
            t.b = self.b * other.a
            t.value = t.a / t.b
        return t

    def __str__(self):
        if self.a < 0 and self.b < 0:
            self.a *= (-1)
            self.b *= -1
        return '{}/{}'.format(self.a, self.b)