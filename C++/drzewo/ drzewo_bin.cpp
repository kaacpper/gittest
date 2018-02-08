/*
 *  drzewo_bin.cpp
 */


#include <iostream>
using namespace std;

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
} *korzen = NULL; // definicja struktury i utworzenie wskaźnika korzeń

Wezel* stworzWezel(int wartosc) {
    Wezel *nowyWezel = new Wezel;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy= NULL;
    
    return nowyWezel;
}

void dodajWezel(Wezel *wezel, int wezel) {
    if (korzen == NULL) {
        korzen = stworzWezel(wartosc);
    } else {
        if (wartosc < wezel->wartosc) {
            if(wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc);
            }
        } else {
            ;
        }
    }
}


int main(int argc, char **argv)
{
	
	return 0;
}

