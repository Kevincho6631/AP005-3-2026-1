#include <iostream>

using namespace std;

int main() {

    int valor;

    cout << "Digite un numero entero: ";
    cin >> valor;

    // Evaluación de paridad
    bool esPar = (valor % 2 == 0);

    cout << "\nResultado:\n";
    cout << "El numero " << valor << " es ";

    if (esPar) {
        cout << "PAR";
    } else {
        cout << "IMPAR";
    }

    cout << endl;

    return 0;
}
