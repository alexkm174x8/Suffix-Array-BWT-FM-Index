# Suffix Array, Burrows-Wheeler Transform (BWT), FM-Index y Búsqueda de Patrones

Alejandro Kong Montoya A01734271 \
Estefania Antonio Villaseca A01736897 \
Miranda Eugenia Colorado Arroniz  A01737027 
##


Conversación con ChatGPT: https://chatgpt.com/share/66f89bd5-b1e4-8004-ba1f-63878e3ba1e8

Este proyecto implementa el Suffix Array, Burrows-Wheeler Transform (BWT) y FM-Index, junto con métodos para realizar la búsqueda de patrones en una cadena de texto. El código está diseñado para leer un archivo de texto, calcular el Suffix Array y la BWT, y permitir la búsqueda eficiente de patrones utilizando el FM-Index.

Además, se realizó un análisis sobre una cadena de genoma, donde se buscó específicamente la subcadena TCGA para verificar su presencia en la secuencia genómica. Este análisis es útil para identificar patrones o secuencias de interés dentro de datos biológicos, como los que se encuentran en secuencias genómicas, proporcionando una herramienta valiosa para investigaciones en bioinformática y genética.

## Archivos del Proyecto

- **SuffixArray.py**: Contiene el código para construir el Suffix Array a partir de una cadena de texto.
- **BWT.py**: Contiene la implementación de la Burrows-Wheeler Transform y sus estructuras de datos asociadas (C y Occur).
- **FMIndex.py**: Contiene la implementación de la búsqueda de patrones utilizando el FM-Index y la función `backwardSearch`.

## Funciones Principales

### 1. `build_suffix_array(text)`
Genera el Suffix Array para una cadena dada.

- **Entrada**: Una cadena de texto `text`.
- **Salida**: El Suffix Array correspondiente.
- **Complejidad Temporal**: O(n log n), debido a la ordenación de sufijos.
- **Complejidad Espacial**: O(n).

---

### 2. `build_bwt(text, suffix_array)`
Genera la Burrows-Wheeler Transform (BWT) a partir de una cadena y su Suffix Array.

- **Entrada**: La cadena `text` y su Suffix Array.
- **Salida**: La BWT de la cadena.
- **Complejidad Temporal**: O(n).
- **Complejidad Espacial**: O(n).

---

### 3. `build_c_array(bwt)`
Construye el arreglo C para la BWT, que indica las posiciones iniciales de cada carácter en la BWT ordenada.

- **Entrada**: La cadena BWT.
- **Salida**: El arreglo C como un diccionario.
- **Complejidad Temporal**: O(n log n), por la ordenación de la BWT.
- **Complejidad Espacial**: O(σ), donde σ es el número de caracteres únicos.

---

### 4. `build_occur_table(bwt)`
Construye la tabla Occur que registra la frecuencia acumulada de cada carácter en la BWT hasta cada posición.

- **Entrada**: La cadena BWT.
- **Salida**: La tabla Occur como un diccionario de listas.
- **Complejidad Temporal**: O(n * σ).
- **Complejidad Espacial**: O(n * σ).

---

### 5. `inverse_bwt(bwt)`
Reconstruye la cadena original a partir de la Burrows-Wheeler Transform.

- **Entrada**: La cadena BWT.
- **Salida**: La cadena original reconstruida.
- **Complejidad Temporal**: O(n).
- **Complejidad Espacial**: O(n + σ).

---

### 6. `backward_search(bwt, c, occur, pattern)`
Implementa la búsqueda hacia atrás utilizando el FM-Index para encontrar un patrón en la cadena original.

- **Entrada**: La cadena BWT, los arreglos C y Occur, y el patrón a buscar.
- **Salida**: El rango de posiciones donde se encuentra el patrón en la cadena original o -1 si no se encuentra.
- **Complejidad Temporal**: O(m * σ), donde m es el tamaño del patrón.
- **Complejidad Espacial**: O(1).


##

# Conclusiones Individuales

#### Alejandro Kong: 
Esta actividad me permitió explorar conceptos avanzados de búsqueda de subcadenas, como el Suffix Array, la Burrows-Wheeler Transform (BWT) y el FM-Index. Colaborar en equipo y utilizar Git fue esencial para organizar nuestro trabajo y documentar el proceso.\
En este caso me toco implementar el Suffix Array, con la ayuda de ChatGPT, facilitó mi comprensión de cómo estas estructuras optimizan la búsqueda en cadenas largas. También aprendí a analizar la complejidad temporal y espacial de nuestros algoritmos, lo que es crucial para mejorar su eficiencia. Esta experiencia me ayudó a reforzar mis conocimientos en estructuras de datos y a apreciar el valor de los grandes modelos de lenguaje en la programación.

#### Miranda Arróniz:
En la actividad de búsqueda en cadenas como el FM-Index, Burrows-Wheeler Transform (BWT) y Suffix Arrays, me enfoqué en implementar el BWT con la ayuda de ChatGPT-4. Contar con la ayuda de ChatGPT fue útil para entender cómo estas estructuras optimizan la búsqueda de datos. También comparé en tiempo y espacio la eficiencia del BWT con los algoritmos que mis demás compañeros implementamos. También use Git para coordinar y documentar el proyecto. Al final, esta experiencia me demostró lo útil que es la IA en programación y aprendizaje.
