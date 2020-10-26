from PatoBorracha import PatoBorracha
from PatoBravo import PatoBravo
from PatoCorredor import PatoCorredor
from PatoRuivo import PatoRuivo
from VoarFoguete import VoarFoguete

class Main:
 
    @staticmethod
    def run():
        pato = PatoRuivo()
        patoCorredor = PatoCorredor()		
        print(pato.mostrar())
        print(pato.nadar())
        print(pato.comportamentoPato())
        pato.setComportamento(VoarFoguete())
        print(pato.comportamentoPato())
        
        print(patoCorredor.correr())

Main().run()
