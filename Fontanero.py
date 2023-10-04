import itertools

def calcular_tiempo_promedio(reparaciones):
    n = len(reparaciones)
    suma_tiempo = sum(reparaciones)
    tiempo_promedio = suma_tiempo / n
    return tiempo_promedio

def orden_optimo_reparaciones(reparaciones):
    mejor_permutacion = None
    mejor_tiempo_promedio = float('inf')
    
    for permutacion in itertools.permutations(reparaciones):
        tiempo_promedio = calcular_tiempo_promedio(permutacion)
        if tiempo_promedio < mejor_tiempo_promedio:
            mejor_tiempo_promedio = tiempo_promedio
            mejor_permutacion = permutacion
    
    return mejor_permutacion, mejor_tiempo_promedio

# Ejemplo de uso:
tiempos_reparacion = [10, 8, 6, 7]
mejor_secuencia, tiempo_minimo_espera = orden_optimo_reparaciones(tiempos_reparacion)
print("Mejor secuencia de reparaciones:", mejor_secuencia)
print("Tiempo mínimo de espera promedio:", tiempo_minimo_espera)