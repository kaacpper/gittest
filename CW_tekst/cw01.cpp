/*
 * cw01.cpp
 */


#include <string>
#include <iostream>

using namespace std;

int main()
{
        string tekst;
        int dlugosc;
        cout << "Podaj tekst, ktory ma zostac odwrocony: " << endl;
        cin >> tekst;

        dlugosc = tekst.length();

        for(int i=dlugosc; i>=0; i--){
            cout << tekst[i];
}

        return 0;
}

