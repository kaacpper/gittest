#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  HELLO.py
#  
#  Copyright 2017  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
rok = 2017
py = 1991

def parzyste (n):
    ile = list(range(0, n+1, 2))
    print(ile)
    return len(ile)

def main(args):
    return 0

if __name__ == '__main__':
    
    imie = input("Podaj imię ")
    print ("HELLO", imie)
    
    wiek = int(input("Ile masz lat?"))
    print ("Masz", wiek, "lat i urodziles sie w", 2017 - wiek, "roku")
    
    if wiek < (rok - py):
        print ("Jestem starszy")
    elif wiek > (rok - py):
        print ("Jestem mlodszy")
    else:
        print ("Mamy tyle samo lat")
        
    n = int(input("Podaj liczbe: "))
    print("Parzystych:", parzyste(n))
    
    import sys
    sys.exit(main(sys.argv))
