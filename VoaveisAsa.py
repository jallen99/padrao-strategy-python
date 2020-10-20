from PadraoVoaveis import PadraoVoaveis


class VoaveisAsa(PadraoVoaveis):
	def __init__(self):
	    self.velocidade = 10

	def voar(self):
		return "Voando como um pássaro que voa. Velocidade: {}".format(self.getVelocidade())

	def getVelocidade(self):
		return self.velocidade
