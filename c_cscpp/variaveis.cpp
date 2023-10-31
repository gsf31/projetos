#include <iostream>
using namespace std;
int main(){

    //TIPO NOME;
    //TIPO NOME = VALOR;

    int vidas=0; //10, 25
    char letra='B'; //'A', 'B', 'C'
    double decimal=5.2; //2.49999999
    float decimal2=5.2; //2.5
    bool vivo=true; //true or false
    string nome="Gustavo"; //"recebe texto"

    cout << "Digite a quantidade de vidas: ";
    cin >> vidas;
    cout << "Digite uma letra: ";
    cin >> letra;
    cout << "Quantos reais tem na carteira: ";
    cin >> decimal;
    cout << "Digite seu nome: ";
    cin >> nome;

    cout <<"\nVidas: " << vidas << "\nLetra:" << letra << "\nDinheiro: " << decimal << "\n" << vivo << "\nNome:" << nome << "\n";

    return 0;
}

