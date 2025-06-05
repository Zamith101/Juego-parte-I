# Juego-parte-I
## Descripcion

Este proyecto consiste en el desarrollo de un juego de batalla por turnos utilizando Python y el paradigma de Programación Orientada a Objetos (POO), con una interfaz gráfica minimalista implementada mediante la librería tkinter. El objetivo del juego es simular un combate entre dos personajes seleccionados por el usuario, de entre tres clases disponibles: Guerrero, Mago y Arquero.

Características del Juego:
Clases y Herencia:

Se define una clase base Personaje que encapsula los atributos comunes: vida, ataque y defensa.

A partir de esta clase se derivan las subclases Guerrero, Mago y Arquero, cada una con su propia lógica de ataque, implementando el concepto de polimorfismo.

Encapsulamiento:

Los atributos de los personajes son privados y se accede a ellos mediante getters y setters.

La vida de los personajes está restringida al rango [0, 100], validado por su setter.

Lógica de Combate:

Cada tipo de personaje tiene una habilidad especial:

Guerrero: Su ataque tiene un 20% más de daño.

Mago: Su ataque ignora la defensa del enemigo.

Arquero: Si su ataque es mayor que la defensa del enemigo, inflige el doble de daño.

Los personajes se atacan por turnos hasta que uno de los dos llega a 0 de vida.

Interfaz Gráfica (Tkinter):

Un menú principal permite seleccionar el tipo de personaje para cada jugador mediante listas desplegables.

Una pantalla de batalla muestra la vida actual de cada personaje, un registro del combate en tiempo real y un botón para ejecutar el ataque por turnos.

Al finalizar la batalla, se muestra automáticamente el ganador.

Validación y Control del Juego:

El juego controla que ningún personaje tenga vida negativa y finaliza correctamente la partida cuando un personaje es derrotado.

Se evita la ejecución del botón de ataque una vez terminada la batalla.
