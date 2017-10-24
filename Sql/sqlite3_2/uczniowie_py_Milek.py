#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uczniowie_py.py
import sqlite3

def wyniki(cur):
    wyniki = cur.fetchall() # pobierz wszystkie wiersze
    for row in wyniki:
        print(tuple(row))

def kw_a(cur):
    cur.execute("""
    SELECT imie, nazwisko, klasa
    FROM tbUczniowie, tbKlasy
    WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
    AND Klasa = '1A'
    """)

    wyniki(cur)
        

def kw_b(cur):
    cur.execute("""
    SELECT MAX (egzhum)
    FROM tbUczniowie
    """)

    wyniki(cur)

def kw_c(cur):
    cur.execute("""
    SELECT AVG(egzmat)
    FROM tbUczniowie, tbKlasy
    WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
    AND Klasa = '1A'
    """)
    wyniki(cur)
    
def kw_d(cur):
    cur.execute("""
    SELECT ocena, imie, nazwisko
    FROM tbOceny, tbUczniowie
    WHERE tbUczniowie.IDUcznia = tbOceny.UczenID
    AND imie = 'Dorota'
    """)

    wyniki(cur)
        
def kw_e(cur):
    cur.execute("""
    SELECT AVG(ocena)
    FROM tbOceny
    WHERE PrzedmiotID = 6
    AND strftime('%m', datad) LIKE '10'    
    """)
    
    wyniki(cur)
        
def kw_f(cur):
    cur.execute("""
    UPDATE tbUczniowie
    SET Egzjez = ?
    WHERE imie = ?
    AND nazwisko = ?
    """, [35, "Paulina", "Dziedzic"])
    cur.execute("""
    SELECT EgzJez
    FROM tbUczniowie
    WHERE imie = "Paulina"
    AND nazwisko = "Dziedzic"
    """)
    
def kw_g(cur):
    cur.execute("""
    DELETE FROM tbOceny
    WHERE ocena = '1'
    WHERE imie = 'Paulina'
    AND nazwisko = 'Dziedzic'
    
    """)

    wyniki(cur)
    
def dodaj(cur):
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?, ?, ?, ?)
    """, [None, '3C', 2015, 2017])
    
def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE idklasy = ?
    """, ['3D', 13])

def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?', ['3D', 2015])

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row
   
   kw_f(cur) 
   # dodaj(cur)
   # aktualizuj(cur)
   # usun(cur)
   # con.commit()
   # wyniki(cur.execute('SELECT * FROM tbKlasy'))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
