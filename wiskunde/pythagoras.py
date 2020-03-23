def bereken_pythagoras(a, b):
    c_kwadraad = a*a + b*b
    c = c_kwadraad ** 0.5  # De wortel van c is hetzelfde als c tot de macht een half
    return c


getal = bereken_pythagoras(3, 4)
print(getal)

print(bereken_pythagoras(7, 10))
