while True:
    entrada = input("Ingrese un número (o 'salir'): ")
    
    if entrada.lower() == "salir":
        break
    
    if not entrada.lstrip("-").isdigit():
        print("❌ Entrada inválida")
        continue
    
    numero = int(entrada)
    
    print(f"El número {numero} es {'Par' if numero % 2 == 0 else 'Impar'}")
