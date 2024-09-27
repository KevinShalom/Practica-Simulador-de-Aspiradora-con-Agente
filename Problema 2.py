import random

class SimuladorAspiradora:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = self.generar_entorno()
        self.posicion_aspiradora = [0, 0]  # Posicion inicial en [fila, columna]
        self.casillas_sucias = sum([fila.count('S') for fila in self.matriz])
        self.movimientos = 0
        self.puntuacion = 0  # Puntuacion del agente

    def generar_entorno(self):
        # 'L' para limpio, 'S' para sucio, 'V' para vacio
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
                print(f'[{i},{j}:{celda}]', end=" ")
            print()
        print(f"\nPosición actual de la aspiradora: {self.posicion_aspiradora}")
        print(f"Movimientos realizados: {self.movimientos}")
        print(f"Puntuación actual del agente: {self.puntuacion}\n")

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
            self.puntuacion += 1  # Ganar +1 por limpiar una celda sucia

    def obtener_estado_actual(self):
        # Devuelve el estado de la celda actual
        fila, columna = self.posicion_aspiradora
        return self.matriz[fila][columna]

class AgenteReactivo:
    def __init__(self, simulador):
        self.simulador = simulador

    def actuar(self):
        # El agente actúa dependiendo del estado de la celda actual
        estado_actual = self.simulador.obtener_estado_actual()
        if estado_actual == 'S':  # Si la celda está sucia, la limpia
            self.simulador.limpiar()
        else:
            # Mover el agente en forma de zigzag por filas (derecha en una fila, izquierda en la siguiente)
            fila, columna = self.simulador.posicion_aspiradora
            if fila % 2 == 0:  # Si estamos en una fila par, movemos a la derecha
                if columna < self.simulador.columnas - 1:
                    self.simulador.mover("derecha")
                else:
                    self.simulador.mover("abajo")  # Al final de la fila, bajamos
            else:  # Si estamos en una fila impar, movemos a la izquierda
                if columna > 0:
                    self.simulador.mover("izquierda")
                else:
                    self.simulador.mover("abajo")  # Al principio de la fila, bajamos

    def ejecutar(self):
        while self.simulador.casillas_sucias > 0:
            self.simulador.imprimir_matriz()
            self.actuar()
        print("¡Todas las casillas sucias han sido limpiadas!")
        print(f"Puntuación final del agente: {self.simulador.puntuacion}")

# Ejemplo de simulación con configuración media global
def simular_agente_en_varias_configuraciones(num_simulaciones, filas, columnas):
    puntuaciones = []
    for i in range(num_simulaciones):
        print(f"\n--- Simulación {i + 1} ---")
        simulador = SimuladorAspiradora(filas, columnas)
        agente = AgenteReactivo(simulador)
        agente.ejecutar()
        puntuaciones.append(simulador.puntuacion)
    
    # Calcular la configuración media global
    puntuacion_media = sum(puntuaciones) / num_simulaciones
    print(f"\nPuntuación media global tras {num_simulaciones} simulaciones: {puntuacion_media}")

# Ejecutar el agente en múltiples configuraciones
simular_agente_en_varias_configuraciones(3, 5, 5)
