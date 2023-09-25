#!/usr/bin/python3

def pow(a, b):
    resultat = 1

    if a == 0 and b == 0:
        return 0
    
    if b < 0:
        a = 1 / a
        b = -b
        resultat = 1.0

    for _ in range(b):
        resultat *= a

    return resultat
