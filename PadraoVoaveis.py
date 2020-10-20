from abc import ABC, abstractmethod


class PadraoVoaveis(ABC):

    @abstractmethod
    def voar(self):
        pass

    @abstractmethod
    def getVelocidade(self):
        pass
