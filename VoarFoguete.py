from PadraoVoaveis import PadraoVoaveis


class VoarFoguete(PadraoVoaveis):

	def __init__ (self):
	    self.velocidade = 1000	
	
	def voar(self):
		return "Voando como um foguete. Velocidade: {}".format(self.getVelocidade())	

	def getVelocidade(self):
		return self.velocidade
