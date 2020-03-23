def bereken_priemgetallen(aantal_getallen):
    """Gebaseerd op: https://nl.wikipedia.org/wiki/Zeef_van_Eratosthenes"""

    getallen = list(range(2, aantal_getallen+1))  # Maakt een lijst van 2 tot en met aantal_getallen

    k = 2
    while k <= aantal_getallen**0.5:  # Zolang k kleiner of gelijk is dan de wortel van aantal_getallen
        for getal in range(k**2, aantal_getallen+1, k):  # Vanaf k**2 tot aantal_getallen+1 in stappen van k
            getallen[getal-2] = False  # -2 aangezien zeef alle waarden (2..n) bevat
        k += 1

    priemgetallen = [getal for getal in getallen if getal]  # Verwijder alle waarden die False zijn
    return priemgetallen


maximum_getal = 11
priemgetallen = bereken_priemgetallen(maximum_getal)

print("De volgende getallen tot en met", maximum_getal, "zijn priemgetallen:")
print(priemgetallen)
print("Dit zijn", len(priemgetallen), "getallen.")
print("Opgeteld is dit", sum(priemgetallen))
