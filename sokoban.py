class Sokoban:

    """
    0 - personaje
    1 - caja
    2 - pared
    3 - meta
    4 - camino
    5 - caja/meta
    6 - personaje/meta
    """

    def __init__(self) -> None:
        # Definir el mapa
        self.mapa = [
            [2,2,2,2,2,2,2,2,2,2,2],
            [2,4,4,4,4,4,4,4,4,4,2],
            [2,4,4,4,4,4,1,4,4,4,2],
            [2,4,4,0,1,4,3,4,4,4,2],
            [2,4,4,4,4,4,4,4,4,4,2],
            [2,4,4,4,4,3,4,4,4,4,2],
            [2,4,4,4,4,4,4,4,4,4,2],
            [2,4,4,4,4,4,4,4,4,4,2],
            [2,2,2,2,2,2,2,2,2,2,2]
        ]
        # Definir la posición inicial del personaje
        self.personaje_fila = 3
        self.personaje_columna = 3
        
    def imprimirMapa(self) -> None:
        # Toma cada fila del mapa y la imprime
        for fila in self.mapa:
            print(fila)
            
    def derecha(self) -> None:
        # 1. Personaje en camino -> personaje en camino (0,4) -> (4,0)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 2. Personaje en meta -> personaje en camino (6,4) -> (3,0)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1
            
        # 3. Personaje en camino -> personaje en meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1
            
        # 4. Personaje empujando la caja -> Personaje empujando la caja (0,1,4) -> (4,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 5. Personaje empujando la caja hacia la meta -> Personaje y caja/meta (0,1,3) -> (4,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 6. Personaje empujando la caja/meta hacia el camino -> Personaje/meta y caja (0,5,4) -> (4,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 7. Personaje/meta empujando la caja -> Personaje empujando la caja (6,1,4) -> (3,0,1) 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 8. Personaje en meta -> personaje en meta (6,3) -> (3,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 9. Personaje empujando la caja/meta hacia la meta -> (0,5,3) -> (4,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 10. Personaje/meta empujando la caja hacia la meta -> (6,1,3) -> (3,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 11. Personaje/meta empujando la caja/meta hacia el camino -> (6,5,4) -> (3,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        # 12. Personaje/meta empujando la caja/meta hacia la meta -> (6,5,3) -> (3,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna + 1

    def izquierda(self) -> None:
        # 1. Personaje en camino -> personaje en camino (4,0) -> (0,4)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 2. Personaje en meta -> personaje en camino (4,6) -> (0,3)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 3. Personaje en camino -> personaje en meta (3,0) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 4. Personaje en meta -> personaje en meta (3,6) -> (6,3)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1
            
        # 5. Personaje empujando la caja -> personaje empujando la caja (4,1,0) -> (1,0,4)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 6. Personaje empujando la caja hacia la meta -> Personaje y caja/meta (3,1,0) -> (5,0,4)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 7. Personaje/meta empujando la caja/meta hacia el camino -> (4,5,6) -> (1,6,3)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 8. Personaje empujando la caja/meta hacia la meta -> (3,5,0) -> (5,6,4)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 9. Personaje/meta empujando la caja -> Personaje empujando la caja (4,1,6) -> (1,0,3) 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 10. Personaje/meta empujando la caja hacia la meta -> (3,1,6) -> (5,0,3)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 11. Personaje empujando la caja/meta hacia el camino -> (4,5,0) -> (1,6,4)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        # 12. Personaje/meta empujando la caja/meta hacia la meta -> (3,5,6) -> (5,6,3)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_columna = self.personaje_columna - 1

    def arriba(self) -> None:
        # 1. Personaje en camino -> personaje en camino (0,4) -> (4,0)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 2. Personaje en meta -> personaje en camino (6,4) -> (3,0)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 3. Personaje en camino -> personaje en meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1
            
        # 4. Personaje empujando la caja -> personaje empujando la caja (0,1,4) -> (4,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1
            
        # 5. Personaje empujando la caja hacia la meta -> Personaje y caja/meta (0,1,3) -> (4,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1
            
        # 6. Personaje empujando la caja/meta hacia el camino -> Personaje/meta y caja (0,5,4) -> (4,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 7. Personaje/meta empujando la caja -> Personaje empujando la caja (6,1,4) -> (3,0,1) 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 8. Personaje en meta -> personaje en meta (6,3) -> (3,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 9. Personaje empujando la caja/meta hacia la meta -> (0,5,3) -> (4,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 10. Personaje/meta empujando la caja hacia la meta -> (6,1,3) -> (3,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 11. Personaje/meta empujando la caja/meta hacia el camino -> (6,5,4) -> (3,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        # 12. Personaje/meta empujando la caja/meta hacia la meta -> (6,5,3) -> (3,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila - 1
                    
    def abajo(self) -> None:
        # 1. Personaje en camino -> personaje en camino (0,4) -> (4,0)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 2. Personaje en meta -> personaje en camino (6,4) -> (3,0)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba el camino
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 3. Personaje en camino -> personaje en meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1 
            
        # 4. Personaje empujando la caja -> personaje empujando la caja (0,1,4) -> (4,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 5. Personaje empujando la caja hacia la meta -> Personaje y caja/meta (0,1,3) -> (4,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 6. Personaje empujando la caja/meta hacia el camino -> Personaje/meta y caja (0,5,4) -> (4,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 7. Personaje/meta empujando la caja -> Personaje empujando la caja (6,1,4) -> (3,0,1) 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 8. Personaje en meta -> personaje en meta (6,3) -> (3,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 9. Personaje empujando la caja/meta hacia la meta -> (0,5,3) -> (4,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3
        ):
            # Coloca un camino donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 10. Personaje/meta empujando la caja hacia la meta -> (6,1,3) -> (3,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la caja
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 11. Personaje/meta empujando la caja/meta hacia el camino -> (6,5,4) -> (3,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Coloca la caja donde estaba el camino
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        # 12. Personaje/meta empujando la caja/meta hacia la meta -> (6,5,3) -> (3,6,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 3
        ):
            # Coloca una meta donde estaba el personaje
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            # Coloca el personaje donde estaba la meta
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 6
            # Coloca la caja en la meta
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 5
            # Actualiza la nueva posición del personaje
            self.personaje_fila = self.personaje_fila + 1

    def verificarVictoria(self) -> None:
        # Revisa todo el mapa: si todavía hay alguna caja (1), no hace nada
        for fila in self.mapa:
            if 1 in fila:
                return None
        
        # Si ya no hay ningún 1, imprime y termina el juego
        print("¡Ganaste!")
        exit()

    def jugar(self) -> None:
        """
        a - izquierda
        d - derecha
        w - arriba
        s - abajo
        """
        while True:
            self.imprimirMapa()
            self.verificarVictoria()

            movimiento = input("Movimiento: ")
            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.izquierda()
            elif movimiento == "w":
                self.arriba()
            elif movimiento == "s":
                self.abajo()
                
soko = Sokoban()
soko.jugar()