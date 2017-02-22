#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Konwersja liczby dziesiętnej na system o podanej podstawie
# <eCG>

cyfry = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
cyfry2 = {v: k for k, v in cyfry.items()}


def do10(liczba, podst):
    liczba = str(liczba)
    potega = len(liczba) - 1
    for cyfra in liczba:
        print int(cyfra) * podst**potega
        potega -= 1


def konwertuj(liczba, podst):

    global cyfry
    liczba = int(liczba)

    reszty = []  # pusta lista
    while liczba > 0:
        reszta = liczba % podst
        reszty.append(reszta)
        liczba = liczba / podst

    reszty.reverse()
    if podst > 10:
        reszty = [cyfry[x] if x > 9 else x for x in reszty]

    return reszty


def main(args):
    liczba = raw_input("Podaj liczbę: ")
    podst = int(raw_input("Podaj podstawę (2-16): "))

    print "".join(str(x) for x in konwertuj(liczba, podst))
    print do10(liczba, podst)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
