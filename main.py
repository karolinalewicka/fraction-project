

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

assert gcd(20, 10) == 10
assert gcd(60, 48) == 12

class Fraction:
    def __init__(self, numerator, denominator):
            self. numerator = numerator
            self.denominator = denominator


    def __eq__(self, other):
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )



    def __add__(self, other):
        new_num = self.numerator*other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    __radd__ = __add__

    def __sub__(self, other):
        new_num = self.numerator*other.denominator - self.denominator * other.numerator  
        new_den = self.denominator * other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    def __rsub__(self, other):
        return -(self.__sub__(other))

    def __mul__(self, other):
        new_num = self.numerator*other.numerator
        new_den = self.denominator*other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    __rmul__ = __mul__

    def __truediv__(self, other):
        new_num = self.numerator*other.denominator
        new_den = self.denominator * other.numerator
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)  
    
    def __rtruediv__(self, other):
        return other * Fraction(self.denominator, self.numerator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

assert Fraction(1, 2) == Fraction(1, 2)
# assert Fraction(1, 3) == Fraction(2, 6)

assert Fraction(1, 4) + Fraction(1, 2) == Fraction(3, 4)
assert 2 + Fraction(1, 2) == Fraction(5, 2)
assert Fraction(1, 2) + 2 == Fraction(5, 2)

assert Fraction(2, 3) - Fraction(1, 2) == Fraction(1, 6)
assert 2 - Fraction(1, 2) == Fraction(3, 2)
assert Fraction(3, 2) - 1 == Fraction(1, 2)

assert Fraction(1, 2) * Fraction(5, 4) == Fraction(5, 8)
assert Fraction(1, 3) * 2 == Fraction(2, 3)
assert 2 * Fraction(1, 3) == Fraction(2, 3)

assert Fraction(1, 4) / Fraction(2, 3) == Fraction(3, 8)
assert Fraction(1, 2) / 2 == Fraction(1, 4)
assert 2 / Fraction(1, 2) == 4
# assert Fraction(1, 4) / Fraction(1, 4) == 1


def convert(expression):
    if "/" in expression:
        left, right = expression.split("/")
        return Fraction(int(left), int(right))
    return int(expression)


assert convert("1") == 1
assert convert("3/4") == Fraction(3, 4)


def evaluate(operator, left, right):
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == ":":
        return left / right
    raise Exception(f"Operator {operator} is not supported")

def calculate(text):
    try:
        left, operator, right = text.split(" ")
        left_fraction, right_fraction = convert(left), convert(right)
        result = evaluate(operator, left_fraction, right_fraction)
        return str(result)
    except:
        return "BLAD"


assert calculate("3 * 8/9") == "8/3"

#
assert calculate("3/4 : 1/2") == "3/2"
assert calculate("1/4 + 1/4") == "1/2"
assert calculate("3/5 - 1/5") == "2/5"
assert calculate("1/3 * 2") == "2/3"
assert calculate("1/0 + 1/4") == "BLAD"
#

def main():
    while True:
        try:
            data = input("")
            print(calculate(data))
        except EOFError:
            break


if __name__ == "__main__":
    main()
