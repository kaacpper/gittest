/*
 * cw02.cpp
 */


#include<iostream>
using namespace std;

int main()
{
    int x=1;
    string tekst;
    cout<<"Wprowadz tekst:\n";
    getline(cin,tekst);

    int l=tekst.length();

    for (int i=0;i<l;i++)
    {
        if (tekst[i]==' ')
        x++;
        cout << tekst[i] << endl;

    }
    cout<<"Ilosc wyrazow wynosi: "<<x;
    return 0;
}



