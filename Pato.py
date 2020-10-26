from abc import ABC, abstractmethod
from PadraoVoaveis import PadraoVoaveis
from PadraoCorrer import PadraoCorrer


class Pato(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
    def nadar(self):
        return "Pato Nadando."
	
    def setComportamento(self, padrao):
        if not isinstance(padrao, PadraoVoaveis):
            raise Exception("Parâmetro padrao deve ser do tipo PadraoVoaveis") 
        self.padraoVoaveis = padrao	
        
    def comportamentoPato(self):
        return self.padraoVoaveis.voar()

    def setPadraoCorrer(self, padrao):
        if not isinstance(padrao, PadraoCorrer):
            raise Exception("Parâmetro padrao deve ser do tipo PadraoCorrer") 
        self.padraoCorrer = padrao
    
    def correr(self):
        return self.padraoCorrer.correr()
