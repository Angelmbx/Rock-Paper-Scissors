
Práctica Agentes Inteligentes
=============================
En esta práctica se desarrollará y analizará el entorno, funcionamiento y estrategias de diseño implementadas en un agente inteligente diseñado para jugar al Piedra - papel - tijera construido en Python.

## Tabla de propiedades del entorno
Contorno de tareas | Observable| Agentes | Determinista | Episódico | Estático | Discreto | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 RPS | Parcialmente | MultiAgente | No determinista | Secuencial | Estático |  Discreto |  Conocido |

 ### Justificación

- _Parcialmente Observable_: el agente no conoce qué decisión tomará el oponente antes de hacer su elección, la observabilidad está limitada a los resultados de los turnos anteriores.

- _Multi-agente_: El juego de piedra, papel o tijera involucra a al menos dos jugadores.

- _No determinista_: No se conoce en qué estado se encontrará "el mundo" una vez el agente tome una decisión, ya que dependerá de la elección del rival, la cual puede ser aleatoria o impredecible.

- _Secuencial_: Considero que se pueden emplear estrategias en base al historial de elecciones del oponente, por lo que sería posible inferir patrones de comportamiento.

- _Estático_: El estado del entorno no cambia mientras el agente toma su decisión.

- _Discreto_: Las opciones disponibles (piedra, papel o tijera) son finitas y claramente definidas.

- _Conocido_: El entorno es conocido porque las reglas del juego no varían y son conocidas por los jugadores.