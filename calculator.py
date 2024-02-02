class Calculator:
    def add(self, x, y):
        """Сложение двух чисел"""
        return x + y

    def subtract(self, x, y):
        """Вычитание одного числа из другого"""
        return x - y

    def multiply(self, x, y):
        """Умножение двух чисел"""
        return x * y

    def divide(self, x, y):
        """Деление одного числа на другое"""
        if y != 0:
            return x / y
        else:
            return "Ошибка: деление на ноль"
