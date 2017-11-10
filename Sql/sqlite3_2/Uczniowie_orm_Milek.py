# -*- coding: utf-8 -*-

from peewee import *

baza_plik = "pracownicy.sqlite3"

baza = SqliteDatabase(baza_plik)  # ':memory:'

class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza

class Klasa(BazaModel):
    id = IntegerField(primary_key=True)
    klasa = CharField(null=False)
    rok_naboru = CharField(null=False)
    rok_matury = CharField(null=False)


class Oceny(BazaModel):
    id = CharField(primary_key=True)
    datad = DATETIME
    UczenId = ForeignKey(uczen)
    PrzedmiotId = IntegerField(null=False)
    Ocena = DecimalField(decimal_places=2)

class Przedmiot(BazaModel):
    id = IntegerField(primary_key=True)
    przedmiot = CharField(null=False)
    NazwiskoNaucz = CharField(null=False)
    ImieNaucz = CharField(null=False)
    PlecNaucz = IntegerField(null=False)


class Uczniowie(BazaModel):
    id = IntegerField(primary_key=True)
    nazwisko = CharField(null=False)
    imie = CharField(null=False)
    plec= IntegerField(null=False)
    KlasaId = IntegerField(null=False)
    EgzHum = DecimalField(decimal_places=2, default=0, null=False)
    EgzMat = DecimalField(decimal_places=2, default=0, null=False)
    EgzJez = DecimalField(decimal_places=2, default=0, null=False)
