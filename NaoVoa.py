from PadraoVoaveis import PadraoVoaveis


class NaoVoa(PadraoVoaveis):
	
	def voar(self):
		return "Esse pato não Voa. Velocidade: {}".format(self.getVelocidade())

	def getVelocidade(self):
		return 0
