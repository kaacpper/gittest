#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uczniowie_py.py
import sqlite3

def kw_a(cur):
    cur.execute("""
    SELECT imie, nazwisko, klasa
    FROM tbUczniowie, tbKlasy
    WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
    AND Klasa = '1A'
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))
        

def kw_b(cur):
    cur.execute("""
    SELECT MAX (egzhum)
    FROM tbUczniowie
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))

def kw_c(cur):
    cur.execute("""
    SELECT AVG(egzmat)
    FROM tbUczniowie, tbKlasy
    WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
    AND Klasa = '1A'
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))
        
def kw_d(cur):
    cur.execute("""
    SELECT ocena, imie, nazwisko
    FROM tbOceny, tbUczniowie
    WHERE tbUczniowie.IDUcznia = tbOceny.UczenID
    AND imie = 'Dorota'
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))
        
def kw_e(cur):
    cur.execute("""
    SELECT AVG(ocena)
    FROM tbOceny
    WHERE Datad = 
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))
        


def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
    
    
    kw_e(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
