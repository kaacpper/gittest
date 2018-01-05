/*
 * struktury.cpp
 */


#include <iostream>
#include <iomanip>
#include <fstream>


using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[30];
    int wiek;
};

struct samochod {
    char marka[40];
    char model[40];
    int rok;
    int przebieg;
};

/*void wyswietlDane(osoba o){
    cout << setw(20) << "Imie: " << o.imie << endl;
    cout << setw(20) << "Nazwisko: " << o.nazwisko << endl;
    cout << setw(20) << "Wiek: " << o.wiek << endl;
}*/

void wyswietlDane(samochod o){
    cout << setw(25) << left << "Marka: " << setfill('.') << o.marka << endl;
    cout << setw(25) << left << "Model: " << setfill('.') << o.model << endl;
    cout << setw(25) << left <<  "Rok produkcji: " << setfill('.') << o.rok << endl;
    cout << setw(25) << left <<  "Przebieg: " << setfill('.') << o.przebieg << endl;
}

void getSamochody(samochod t[], int n){
    for(int i=0; i < n; i++){
        cout << "Podaj marke: ";
        cin >> t[i].marka;
        cout << "Podaj model: ";
        cin >> t[i].model;
        cout << "Podaj rok produkcji: ";
        cin >> t[i].rok;
        cout << "Podaj przebieg: ";
        cin >> t[i].przebieg;
    }
}

void drukujSamochody(samochod t[], int n){
    for(int i=0; i < n; i++){
        cout << setw(25) << left << "Marka: " << setfill('.') << t[i].marka << endl;
        cout << setw(25) << left << "Model: " << setfill('.') << t[i].model << endl;
        cout << setw(25) << left <<  "Rok produkcji: " << setfill('.') << t[i].rok << endl;
        cout << setw(25) << left <<  "Przebieg: " << setfill('.') << t[i].przebieg << endl << endl;
    }
}


void zapiszDane (samochod t[], int n) {
    ofstream plik("samochody.txt", ios::app);
    if (!plik.is_open()) {
        cout << "Błąd otwarcia pliku!";
    } else {
        for(int i=0; i < n; i++) {
            cout << t[i].marka << "," << t[i].model << "," << t[i].rok << "," << t[i].przebieg << endl;
            plik << t[i].marka << "," << t[i].model << "," << t[i].rok << "," << t[i].przebieg << endl;
        }
    }
}


int czytajDane(samochod t[]) {
    ifstream plik("samochody.txt");
    string linia;
    int i = 0;
    
    if (plik.is_open()) {        
        while(getline(plik, linia)) {
            cout << linia << endl;
            i++; //liczymy przeczytane rekordy
        }
    } else {
        cout << "Błąd otwarcia pliku";
    }
    
    return i;
}



int main(int argc, char **argv)
{

    //~osoba uczen1;
    //~cout << "Podaj imie: ";
    //~cin >> uczen1.imie;
    //~cout << "Podaj nazwosko: ";
    //~cin >> uczen1.nazwisko;
    //~cout << "Podaj wiek: ";
    //~cin >> uczen1.wiek;
    
    //~samochod auto1;
    //~cout << "Podaj marke: ";
    //~cin >> auto1.marka;
    //~cout << "Podaj model: ";
    //~cin >> auto1.model;
    //~cout << "Podaj rok produkcji: ";
    //~cin >> auto1.rok;
    //~cout << "Podaj przebieg: ";
    //~cin >> auto1.przebieg;
    
    int n = 3;
    samochod tb[n];
    //getSamochody(tb, n);
    //drukujSamochody(tb, n);
    
    //zapiszDane(tb, n);
	cout << czytajDane(tb) << endl;
    return 0;
}
