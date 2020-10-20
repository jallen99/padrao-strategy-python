from abc import ABC, abstractmethod


class Pato(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
    def nadar(self):
        return "Pato Nadando."
	
    def setComportamento(self, padrao):
        self.padraoVoaveis = padrao	
        
    def comportamentoPato(self):
        return self.padraoVoaveis.voar()
