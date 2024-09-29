# 🧹 Simulador de Aspiradora con Agente Reactivo

## 📝 Descripción

Este proyecto implementa un **simulador de entorno** para una aspiradora controlada por un **agente reactivo**. El entorno es una cuadrícula de celdas que pueden estar en tres estados: limpio (`L`), sucio (`S`), o vacío (`V`). La aspiradora empieza en la esquina superior izquierda y su misión es **limpiar todas las casillas sucias** de la manera más eficiente posible. ¡Incluye una versión con penalización por movimiento!

### 🤖 Agente Reactivo Simple
El agente decide sus acciones dependiendo solo del **estado actual** de la celda en la que se encuentra y sigue un patrón de movimiento en zigzag para cubrir todo el entorno.

### 💡 Agente Reactivo con Penalización
En esta versión, cada movimiento del agente reduce su puntuación, lo que le obliga a minimizar movimientos innecesarios mientras limpia el entorno.

## 🛠️ Estructura del Proyecto

El proyecto tiene las siguientes clases:

1. **SimuladorAspiradoraConPenalizacion**:
   - Crea un entorno aleatorio de celdas de dimensiones variables.
   - Las celdas tienen una probabilidad de ser:
     - 60% limpias (`L`).
     - 30% sucias (`S`).
     - 10% vacías (`V`).
   - La aspiradora puede moverse en cuatro direcciones: `arriba`, `abajo`, `izquierda`, `derecha`.
   - Cada movimiento **penaliza** con -1 punto y cada limpieza suma +1 punto.

2. **AgenteReactivoConPenalizacion**:
   - El agente decide si limpia o se mueve según el estado de la celda actual.
   - Su patrón de movimiento es **zigzag** (derecha en una fila par, izquierda en una fila impar).
   - El objetivo es limpiar todas las celdas sucias con el menor número de movimientos posibles.

3. **SimuladorAspiradora** (versión sin penalización):
   - Versión sin penalización por movimiento.
   - El agente sigue el mismo patrón de zigzag pero sin penalización al moverse.

4. **AgenteReactivo**:
   - Funciona igual que el **AgenteReactivoConPenalizacion**, pero sin el coste por movimiento.

## 🚀 Ejecución del Proyecto

Sigue estos pasos para ejecutar el simulador:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/nombre-repositorio.git
   cd nombre-repositorio
   
2. **Ejecutar una simulación:**
   ```bash
   python simulador_con_penalizacion.py

## 📊 Resultados
Al final de cada simulación, se muestra la puntuación final del agente y el número total de movimientos realizados. También se puede ejecutar varias simulaciones para calcular la puntuación media global.
```bash
--- Simulación 1 ---
Estado actual del entorno:
[0,0:L] [0,1:S] [0,2:L] [0,3:V] [0,4:L]
...
Posición actual de la aspiradora: [0, 0]
Movimientos realizados: 0
Puntuación actual del agente (con penalización): 0

¡Todas las casillas sucias han sido limpiadas!
Puntuación final del agente (con penalización): 15
