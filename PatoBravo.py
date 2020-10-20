from Pato import Pato
from PadraoGrasnar import PadraoGrasnar
from VoaveisAsa import VoaveisAsa


class PatoBravo (Pato, PadraoGrasnar):

	def __init__(self):	
		self.setComportamento(VoaveisAsa())		

	def mostrar(self):	
		return "Eu sou o Pato Bravo."

	def grasnar(self):
		return "Que-Que. Grrrrrrrrr."
