def bereken_proc_ver(oud, nieuw):
    verandering = (nieuw-oud) / oud
    return verandering * 100



oude_waarde = 100
nieuwe_waarde = 110
verandering1 = bereken_proc_ver(oude_waarde, nieuwe_waarde)
print("De procentuele verandering tussen", oude_waarde, "en", nieuwe_waarde, "is", verandering1, "procent.")