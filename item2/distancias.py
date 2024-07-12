# script principal
from Def import obtener_coordenadas, calcular_distancia, calcular_tiempo_y_combustible

while True:
    ciudad_origen = input("Ingrese la ciudad de origen (o 's' para salir): ")
    if ciudad_origen.lower() == 's':
        break

    ciudad_destino = input("Ingrese la ciudad de destino (o 's' para salir): ")
    if ciudad_destino.lower() == 's':
        break

    distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)

    if distancia_km and distancia_millas:
        print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia_km:.2f} kilómetros ({distancia_millas:.2f} millas).")

        velocidad_promedio = float(input("Ingrese la velocidad promedio esperada (en km/h): "))
        consumo_combustible = float(input("Ingrese el consumo de combustible por kilómetro (en litros/km): "))

        tiempo_horas, tiempo_minutos, tiempo_segundos, combustible = calcular_tiempo_y_combustible(distancia_km, velocidad_promedio, consumo_combustible)

        print(f"Tiempo estimado de viaje: {tiempo_horas} horas, {tiempo_minutos} minutos, {tiempo_segundos} segundos.")
        print(f"Combustible necesario: {combustible:.2f} litros.")

        # Narrativa del viaje
        print(f"\nNarrativa del viaje:\nDesde {ciudad_origen} hasta {ciudad_destino}, recorriendo {distancia_km:.2f} kilómetros en aproximadamente {tiempo_horas} horas y {tiempo_minutos} minutos, necesitarás alrededor de {combustible:.2f} litros de combustible.")
    else:
        print("No se pudo obtener la información de una o ambas ciudades. Asegúrate de que los nombres estén escritos correctamente.")
