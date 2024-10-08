import pandas as pd

# Cargar el dataset
df = pd.read_csv('/Users/juanperez/Desktop/IBERO/INTELIGENCIA ARTIFICIAL/ACTIVIDAD 3/dataset_transporte.csv')

# Función para encontrar la mejor ruta
def encontrar_mejor_ruta(estacion_origen, estacion_destino):
    ruta = df[(df['estacion_origen'] == estacion_origen) & (df['estacion_destino'] == estacion_destino)]
    if ruta.empty:
        return f"No se encontró una ruta directa entre {estacion_origen} y {estacion_destino}."
    else:
        distancia = ruta['distancia_km'].values[0]
        costo = ruta['costo'].values[0]
        tiempo = ruta['tiempo_estimado_viaje'].values[0]
        return (f"La mejor ruta desde {estacion_origen} hasta {estacion_destino} "
                f"tiene una distancia de {distancia} km, cuesta {costo} pesos, "
                f"y toma {tiempo} minutos.")

# Probar la función
if __name__ == '__main__':
    estacion_origen = 'A'
    estacion_destino = 'B'
    resultado = encontrar_mejor_ruta(estacion_origen, estacion_destino)
    print(resultado)
