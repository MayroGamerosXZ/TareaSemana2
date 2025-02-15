import random
import string
import time
from typing import List, Dict
import timeit


class Usuario:
    def __init__(self, id: int, nombre: str, edad: int):
        self.id = id
        self.nombre = nombre
        self.edad = edad


def generar_nombre_aleatorio(longitud: int = 8) -> str:
    """Genera un nombre aleatorio de la longitud especificada"""
    return ''.join(random.choices(string.ascii_lowercase, k=longitud)).capitalize()


def generar_usuarios(cantidad: int) -> List[Usuario]:
    """Genera una lista de usuarios con datos aleatorios"""
    usuarios = []
    for i in range(cantidad):
        nombre = generar_nombre_aleatorio()
        edad = random.randint(18, 80)
        usuarios.append(Usuario(i, nombre, edad))
    return usuarios


def busqueda_lineal(usuarios: List[Usuario], id_buscado: int) -> Usuario:
    """Implementa búsqueda lineal para encontrar un usuario por ID"""
    for usuario in usuarios:
        if usuario.id == id_buscado:
            return usuario
    return None


def busqueda_binaria(usuarios: List[Usuario], id_buscado: int) -> Usuario:
    """Implementa búsqueda binaria para encontrar un usuario por ID"""
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


def medir_tiempo_busqueda(usuarios: List[Usuario], id_buscado: int, funcion_busqueda, numero_pruebas: int = 1000):
    """Mide el tiempo de ejecución de una función de búsqueda"""
    tiempo = timeit.timeit(
        lambda: funcion_busqueda(usuarios, id_buscado),
        number=numero_pruebas
    )
    return tiempo / numero_pruebas


def main():
    # Generar usuarios
    print("Generando usuarios...")
    usuarios = generar_usuarios(100000)
    print(f"Se generaron {len(usuarios)} usuarios")

    # ID a buscar (ejemplo: último usuario)
    id_buscar = 99999

    # Medir tiempos de búsqueda
    tiempo_lineal = medir_tiempo_busqueda(usuarios, id_buscar, busqueda_lineal)
    tiempo_binario = medir_tiempo_busqueda(usuarios, id_buscar, busqueda_binaria)

    # Mostrar resultados
    print(f"\nTiempos de búsqueda promedio para ID {id_buscar}:")
    print(f"Búsqueda lineal Realizada: {tiempo_lineal:.6f} segundos")
    print(f"Búsqueda binaria Realizada: {tiempo_binario:.6f} segundos")
    print(f"La búsqueda binaria es {tiempo_lineal / tiempo_binario:.2f} veces más veloz")


if __name__ == "__main__":
    main()