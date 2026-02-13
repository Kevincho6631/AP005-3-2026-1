#include <iostream>

int main() {
    int num1, num2, suma;

    // Solicitar al usuario que ingrese dos números
    std::cout << "Ingrese el primer numero: ";
    std::cin >> num1;
    std::cout << "Ingrese el segundo numero: ";
    std::cin >> num2;

    // Calcular la suma
    suma = num1 + num2;

    // Mostrar el resultado
    std::cout << "La suma es: " << suma << std::endl;

    return 0;
}
