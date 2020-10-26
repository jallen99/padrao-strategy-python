from Pato import Pato
from PadraoGrasnar import PadraoGrasnar
from PadraoCorrer import PadraoCorrer
from VoaveisAsa import VoaveisAsa
from CorrerLento import CorrerLento


class PatoCorredor (Pato, PadraoGrasnar, PadraoCorrer):

	def __init__(self):	
		self.setComportamento(VoaveisAsa())
		self.setPadraoCorrer(CorrerLento())	

	def mostrar(self):	
		return "Eu sou o Pato Bravo."

	def grasnar(self):
		return "Que-Que. Grrrrrrrrr."
