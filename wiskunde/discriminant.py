def bereken_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant


print("De discriminant van a=2, b=3 en c=4 is:")
print(bereken_discriminant(2, 3, 4))

print("De discriminant van a=2, b=4 en c=2 is:", bereken_discriminant(2, 4, 2))
