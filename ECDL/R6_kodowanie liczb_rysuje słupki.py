from turtle import *

bok = 90

def kwadrat(kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        left(90)
    end_fill()

def slupek(k1,k2,k3):
    pd()
    kwadrat(k1)
    pu()
    left(90)
    fd(bok)
    right(90)
    pd()
    kwadrat(k2)
    pu()
    left(90)
    fd(bok)
    right(90)
    pd()
    kwadrat(k3)
    pu()

def sumuj(liczba):
    if liczba > 99 and liczba < 1000:
        jedności = liczba%10
        liczba = (liczba - liczba%10)/10
        dziesiątki = liczba%10
        liczba = (liczba - liczba%10)/10
        setki = liczba
    return jedności + dziesiątki + setki

def koduj_slupek(liczba):
    if sumuj(liczba) >= 1 and sumuj(liczba) <= 5:
        slupek("blue","blue","green")
    if sumuj(liczba) >= 6 and sumuj(liczba) <= 10:
        slupek("blue","green","green")
    if sumuj(liczba) >= 11 and sumuj(liczba) <= 15:
        slupek("green","green","green")
    if sumuj(liczba) >= 16 and sumuj(liczba) <= 20:
        slupek("green","green","blue")
    if sumuj(liczba) >= 21 and sumuj(liczba) <= 25:
        slupek("green","blue","blue")
    if sumuj(liczba) >= 26 and sumuj(liczba) <= 26:
        slupek("blue","blue","blue")

def koduj(a,b,c):
    koduj_slupek(a)
    fd(bok)
    right(90)
    fd(bok*2)
    left(90)
    koduj_slupek(b)
    fd(bok)
    right(90)
    fd(bok*2)
    left(90)
    koduj_slupek(c)
        




