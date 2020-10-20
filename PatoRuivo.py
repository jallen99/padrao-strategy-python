from Pato import Pato
from VoaveisAsa import VoaveisAsa


class PatoRuivo(Pato, VoaveisAsa):
    def __init__(self):
        self.setComportamento(VoaveisAsa())

    def mostrar(self):
        return "Eu sou o Pato Ruivo."

    def grasnar(self):
        return "Que-Que."
