def emparejar_minimizando_suma_maxima(numeros):
    numeros.sort()  # Ordena la lista de números de manera ascendente
    parejas = []

    while len(numeros) >= 2:
        # Toma los dos números más grandes disponibles
        numero1 = numeros.pop()
        numero2 = numeros.pop()
        
        # Forma una pareja y agrega la suma a la lista de parejas
        parejas.append((numero1, numero2))
    
    return parejas

# Ejemplo de uso:
n = 6
numeros = [3.5, 2.5, 4.0, 1.0, 5.5, 0.5]
parejas = emparejar_minimizando_suma_maxima(numeros)
print("Parejas que minimizan la suma máxima:")
for pareja in parejas:
    print(pareja)