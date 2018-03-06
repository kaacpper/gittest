#ifndef DRZEWO_HPP
#define DRZEWO_HPP

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
};

class Drzewo{
private:
    Wezel *lewy;
    Wezel *prawy;
    int stworzWezel(int);				  // aktualna liczba elementow na liscie
public:
    
    Drzewo();
    ~Drzewo();
    
    void Dodaj(int);
    void Wyswietl();
    void Wstaw(int, int); // wstawia element na podanej pozycji
    bool Usun();
};

#endif
