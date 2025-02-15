import random
import string
import time
from typing import List, Dict
import timeit


# Definición de la clase base para almacenar usuarios
class Usuario:
    def __init__(self, id: int, nombre: str, edad: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad


# Funciones de generación de datos
def generar_nombre_aleatorio(longitud: int = 8) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=longitud)).capitalize()


def generar_usuarios(cantidad: int) -> List[Usuario]:
    usuarios = []
    for i in range(cantidad):
        nombre = generar_nombre_aleatorio()
        edad = random.randint(18, 80)
        usuarios.append(Usuario(i, nombre, edad))
    return usuarios


# Algoritmos de búsqueda
def busqueda_lineal(usuarios: List[Usuario], id_buscado: int) -> Usuario:

    #Búsqueda simple: revisa cada usuario uno por uno
       #Complejidad: O(n) - donde n es el número de usuarios """

    for usuario in usuarios:
        if usuario.id == id_buscado:
            return usuario
    return None


def busqueda_binaria(usuarios: List[Usuario], id_buscado: int) -> Usuario:


    #Búsqueda optimizada: divide la lista en mitades
    #Complejidad: O(log n) - donde n es el número de usuarios
    # Se Requiere que los usuarios estén ordenados por ID

    izquierda, derecha = 0, len(usuarios) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].id == id_buscado:
            return usuarios[medio]
        elif usuarios[medio].id < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None


# Función para medir el rendimiento
def medir_tiempo_busqueda(usuarios: List[Usuario], id_buscado: int, funcion_busqueda, numero_pruebas: int = 1000):
    """
    Mide el tiempo promedio de ejecución realizando múltiples pruebas
    """
    tiempo = timeit.timeit(
        lambda: funcion_busqueda(usuarios, id_buscado),
        number=numero_pruebas
    )
    return tiempo / numero_pruebas


# Programa principal
def main():
    # Configuración inicial
    TOTAL_USUARIOS = 100000
    ID_BUSCAR = 99999  # Caso más desfavorable para búsqueda lineal

    # Generación de datos de prueba
    print("Generando usuarios...")
    usuarios = generar_usuarios(TOTAL_USUARIOS)
    print(f"Se generaron {len(usuarios)} usuarios")

    # Ejecución de pruebas de rendimiento
    tiempo_lineal = medir_tiempo_busqueda(usuarios, ID_BUSCAR, busqueda_lineal)
    tiempo_binario = medir_tiempo_busqueda(usuarios, ID_BUSCAR, busqueda_binaria)

    # Presentación de resultados
    print(f"\nTiempos de búsqueda promedio para ID {ID_BUSCAR}:")
    print(f"Búsqueda lineal: {tiempo_lineal:.6f} segundos")
    print(f"Búsqueda binaria: {tiempo_binario:.6f} segundos")
    print(f"La búsqueda binaria es {tiempo_lineal / tiempo_binario:.2f} veces más rápida")

    for _ in range(5):
        print()
    print(f"Gracias por utilizar este proceso de Busqueda y Moduralizacion")



if __name__ == "__main__":
    main()
