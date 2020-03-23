def maak_fizzbuzz(n):
    """Zie ook: https://en.wikipedia.org/wiki/Fizz_buzz"""

    for getal in range(1, n+1):
        if getal % 3 == 0 and getal % 5 == 0:
            print("FizzBuzz")
        elif getal % 3 == 0:
            print("Fizz")
        elif getal % 5 == 0:
            print("Buzz")
        else:
            print(getal)


maak_fizzbuzz(20)
