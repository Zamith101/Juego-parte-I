import random

class Personaje:
    def __init__(self, vida, ataque, defensa):
        self.__vida = self.__validar_vida(vida)
        self.__ataque = ataque
        self.__defensa = defensa

    def __validar_vida(self, vida):
        return max(0, min(vida, 100))

    def get_vida(self):
        return self.__vida

    def set_vida(self, nueva_vida):
        self.__vida = self.__validar_vida(nueva_vida)

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.__vida > 0

    def atacar(self, objetivo):
        pass 

class Guerrero(Personaje):
    def atacar(self, objetivo):
        daño = int(self.get_ataque() * 1.2) - objetivo.get_defensa()
        daño = max(0, daño)
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"Guerrero ataca con fuerza incrementada. Daño: {daño}"

class Mago(Personaje):
    def atacar(self, objetivo):
        daño = self.get_ataque()  # Ignora defensa
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"Mago lanza un hechizo. Daño: {daño} (ignora defensa)"

class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.get_ataque() > objetivo.get_defensa():
            daño = (self.get_ataque() - objetivo.get_defensa()) * 2
        else:
            daño = self.get_ataque() - objetivo.get_defensa()
        daño = max(0, daño)
        objetivo.set_vida(objetivo.get_vida() - daño)
        return f"Arquero dispara flecha precisa. Daño: {daño}"

import tkinter as tk
from tkinter import ttk

clases = {
    "Guerrero": lambda: Guerrero(100, 40, 60),
    "Mago": lambda: Mago(70, 60, 30),
    "Arquero": lambda: Arquero(80, 55, 40)
}

class JuegoBatalla:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Batalla")
        self.jugador1 = None
        self.jugador2 = None
        self.setup_menu()

    def setup_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Selecciona los personajes", font=("Arial", 16)).pack(pady=10)

        self.personaje1 = tk.StringVar()
        self.personaje2 = tk.StringVar()
        self.personaje1.set("Guerrero")
        self.personaje2.set("Mago")

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Jugador 1").grid(row=0, column=0, padx=10)
        tk.OptionMenu(frame, self.personaje1, *clases.keys()).grid(row=1, column=0)

        tk.Label(frame, text="Jugador 2").grid(row=0, column=1, padx=10)
        tk.OptionMenu(frame, self.personaje2, *clases.keys()).grid(row=1, column=1)

        tk.Button(self.root, text="Iniciar Batalla", command=self.iniciar_batalla).pack(pady=20)

    def iniciar_batalla(self):
        self.jugador1 = clases[self.personaje1.get()]()
        self.jugador2 = clases[self.personaje2.get()]()
        self.batalla_pantalla()

    def batalla_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.log = tk.Text(self.root, height=10, width=60, state='disabled', bg="#f0f0f0")
        self.log.pack(pady=10)

        self.vida1 = tk.Label(self.root, text=f"Jugador 1 ({self.personaje1.get()}): {self.jugador1.get_vida()} HP")
        self.vida1.pack()
        self.vida2 = tk.Label(self.root, text=f"Jugador 2 ({self.personaje2.get()}): {self.jugador2.get_vida()} HP")
        self.vida2.pack()

        self.boton_atacar = tk.Button(self.root, text="Turno de Ataque", command=self.turno)
        self.boton_atacar.pack(pady=10)

        self.turno_jugador = True 

    def turno(self):
        if self.turno_jugador:
            resultado = self.jugador1.atacar(self.jugador2)
        else:
            resultado = self.jugador2.atacar(self.jugador1)

        self.turno_jugador = not self.turno_jugador
        self.mostrar_resultado(resultado)

        if not self.jugador1.esta_vivo() or not self.jugador2.esta_vivo():
            self.boton_atacar.config(state="disabled")
            ganador = "Jugador 1" if self.jugador1.esta_vivo() else "Jugador 2"
            self.mostrar_resultado(f"{ganador} ha ganado la batalla.")

    def mostrar_resultado(self, texto):
        self.log.config(state='normal')
        self.log.insert(tk.END, texto + "\n")
        self.log.see(tk.END)
        self.log.config(state='disabled')

        self.vida1.config(text=f"Jugador 1 ({self.personaje1.get()}): {self.jugador1.get_vida()} HP")
        self.vida2.config(text=f"Jugador 2 ({self.personaje2.get()}): {self.jugador2.get_vida()} HP")


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoBatalla(root)
    root.mainloop()
