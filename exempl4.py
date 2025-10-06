while True:
    print("Posa dos números")
    dad1 = int(input())
    dad2 = int(input())
    dad3 = dad1 + dad2
    print("La suma es:", dad3)
    
    seguir = input("¿Quieres sumar otros números? (s/n): ").lower()
    if seguir != 's':
        print("¡Hasta luego!")
        break
