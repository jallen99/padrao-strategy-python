from Pato import Pato
from NaoVoa import NaoVoa

class PatoBorracha(Pato):

	def __init__(self):
		self.setComportamento(NaoVoa())	
	
	def mostrar(self):
		return "Olá, eu sou de Boarracha."
