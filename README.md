# Sokoban en Python

Se realizó el juego "Sokoban" para que se pueda visualizar en la terminal desarrollado en Python. 

El juego consiste en mover cajas hacia la meta, pero contiene muchos elementos que son importantes, asi que no solo es mover una caja, sino saber como funciona cada función y como se combina cada elemento del juego

## Representación del Mapa

El tablero funciona mediante una matriz, donde cada número representa un elemento específico del juego:

- `0`: Personaje sobre camino libre
- `1`: Caja sobre camino libre
- `2`: Pared (obstáculo que no se puede atravesar)
- `3`: Meta vacía
- `4`: Camino libre por donde se puede caminar
- `5`: Caja colocada correctamente en una meta
- `6`: Personaje parado sobre una meta

## Explicación del Código y Funciones

El programa está organizado en varias funciones dentro de la clase para controlar cada parte del juego:

### 1. `imprimirMapa(self)`
Recorre la matriz mediante un ciclo `for` y la imprime en la consola. Esto permite visualizar el estado del tablero después de cada movimiento del jugador.

### 2. Métodos de movimiento (`derecha`, `izquierda`, `arriba`, `abajo`)
Cada una de estas cuatro funciones se encarga de mover al personaje en su dirección correspondiente. Para evitar que el personaje atraviese paredes o borre elementos por error, cada dirección evalúa **12 casos posibles** mediante una estructura de `if` y `elif`:

- **Movimientos simples:**
  - Moverse de camino a camino: deja un camino (`4`) y avanza (`0`).
  - Salir de una meta a camino: restaura la meta libre (`3`) y avanza a camino (`0`).
  - Entrar de camino a meta: deja un camino (`4`) y pasa a ser personaje en meta (`6`).
  - Moverse de una meta a otra meta vecina: restaura la meta actual (`3`) y ocupa la siguiente (`6`).

- **Empuje de cajas:**
  - Evalúan dos casillas adelante para revisar qué hay detrás de la caja.
  - Empujar caja normal a camino libre o a una meta (cambiando la caja a `1` o `5`).
  - Empujar cajas que ya estaban en una meta hacia afuera a un camino o hacia otra meta.
  - Empujar cajas cuando el propio personaje está parado sobre una casilla de meta (`6`), asegurando que al moverse se restaure la meta (`3`) en la casilla que deja atrás.
  - En cada caso válido, se actualizan los valores numéricos correspondientes en la matriz y se suman o restan las variables `personaje_fila` o `personaje_columna`. Si el movimiento choca con una pared (`2`) o con dos cajas seguidas, ninguna condición se cumple y el personaje simplemente no se mueve.

### 3. `verificarVictoria(self)`
Esta función revisa si el jugador ya completó el nivel. Utiliza un ciclo `for` que revisa cada fila del mapa buscando si todavía existe algún número `1` (caja fuera de meta). Si encuentra al menos una caja con valor `1`, la función termina con `return None` para permitir que el juego continúe. Si ya no encuentra ningún `1` (lo que significa que todas las cajas pasaron al estado `5`), muestra en pantalla el mensaje `¡Ganaste!` y detiene el programa con `exit()`.

### 4. `jugar(self)`
Es el ciclo principal del juego. Contiene un bucle `while True` que repite el flujo en cada turno:
1. Imprime el mapa actual con `self.imprimirMapa()`.
2. Llama a `self.verificarVictoria()` para comprobar si ya se ganó.
3. Solicita una tecla al usuario mediante `input()`.
4. Ejecuta la función de movimiento que corresponda según la tecla ingresada (`w`, `a`, `s`, `d`) o termina el bucle si se presiona `q`.

## Controles del Juego

- `w`: Mover arriba
- `s`: Mover abajo
- `a`: Mover izquierda
- `d`: Mover derecha
- `q`: Salir del juego

## Cómo Ejecutar el Juego

1. Entra a la carpeta donde está el archivo del juego:

```bash
cd sokoban
```

2. Escribe el siguiente comando para poder jugar Sokoban en la terminal:

```bash
python sokoban.py