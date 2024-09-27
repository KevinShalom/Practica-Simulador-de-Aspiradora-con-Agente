import random

class SimuladorAspiradora:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = self.generar_entorno()
        self.posicion_aspiradora = [0, 0]  # Posición inicial en [fila, columna]
        self.casillas_sucias = sum([fila.count('S') for fila in self.matriz])
        self.movimientos = 0

    def generar_entorno(self):
        # 'L' para limpio, 'S' para sucio, 'V' para vacío
        matriz = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                rnd = random.random()
                if rnd < 0.6:
                    fila.append('L')  # 60% limpio
                elif rnd < 0.9:
                    fila.append('S')  # 30% sucio
                else:
                    fila.append('V')  # 10% vacío
            matriz.append(fila)
        return matriz

    def imprimir_matriz(self):
        print("\nEstado actual del entorno:")
        for i, fila in enumerate(self.matriz):
            for j, celda in enumerate(fila):
                # Simplemente mostramos el estado de la celda sin la 'A'
                print(f'[{i},{j}:{celda}]', end=" ")
            print()
        # Mostramos información de la posición actual
        print(f"\nPosición actual de la aspiradora: {self.posicion_aspiradora}")
        print(f"Movimientos realizados: {self.movimientos}\n")

    def mover(self, direccion):
        fila, columna = self.posicion_aspiradora
        if direccion == "arriba" and fila > 0:
            self.posicion_aspiradora[0] -= 1
        elif direccion == "abajo" and fila < self.filas - 1:
            self.posicion_aspiradora[0] += 1
        elif direccion == "izquierda" and columna > 0:
            self.posicion_aspiradora[1] -= 1
        elif direccion == "derecha" and columna < self.columnas - 1:
            self.posicion_aspiradora[1] += 1
        self.movimientos += 1

    def limpiar(self):
        fila, columna = self.posicion_aspiradora
        if self.matriz[fila][columna] == 'S':
            self.matriz[fila][columna] = 'L'
            self.casillas_sucias -= 1

    def ejecutar(self):
        while self.casillas_sucias > 0:
            self.imprimir_matriz()
            accion = input("Ingresa acción (arriba, abajo, izquierda, derecha, limpiar): ").strip().lower()
            if accion in ['arriba', 'abajo', 'izquierda', 'derecha']:
                self.mover(accion)
            elif accion == "limpiar":
                self.limpiar()
        print("¡Todas las casillas sucias han sido limpiadas!")

# Ejemplo de uso
simulador = SimuladorAspiradora(5, 5)
simulador.ejecutar()
