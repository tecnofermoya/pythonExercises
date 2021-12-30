a = 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3
b = 0.3 * 10
print("a:", a)
print("b:", b)
print("Son iguales?", a == b)

import decimal
d = decimal.Decimal("0.3")
a = d + d + d + d + d + d + d + d + d + d
b = d * 10
print("a:", a)
print("b:", b)
print("Con decimal funciona?", a == b)