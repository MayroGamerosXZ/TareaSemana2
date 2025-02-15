# Programa de Búsqueda de Usuarios

Este programa crea una lista de usuarios aleatorios y compara dos métodos diferentes para buscarlos.

## Qué hace el programa

- Crea 100,000 usuarios con nombres aleatorios
- Implementa búsqueda lineal y binaria
- Compara qué método es más rápido
- Muestra los tiempos de cada búsqueda

## Requisitos

- Python 3.6 o superior
- No necesita instalar paquetes adicionales

## Cómo usar el programa

1. Guarda el código en un archivo (ejemplo: `busqueda_usuarios.py`)
2. Abre tu terminal
3. Ejecuta el programa:
   ```bash
   python busqueda_usuarios.py
   ```

## Estructura del código

El programa tiene estas partes principales:
- Clase Usuario: guarda id, nombre y edad
- Generador de usuarios: crea usuarios con datos aleatorios
- Búsqueda lineal: busca revisando uno por uno
- Búsqueda binaria: busca dividiendo la lista en mitades
- Medidor de tiempo: compara la velocidad de cada método

## Ejemplo de salida

```
Generando usuarios...
Se generaron 100000 usuarios

Tiempos de búsqueda promedio para ID 99999:
Búsqueda lineal: 0.003500 segundos
Búsqueda binaria: 0.000005 segundos
La búsqueda binaria es 700.00 veces más rápida
```

## Notas importantes

- La búsqueda binaria es más rápida pero necesita que los datos estén ordenados
- Los tiempos pueden variar según la computadora con la que se realice la búsqueda
- Los nombres generados son aleatorios y no son nombres reales
