from PatoBorracha import PatoBorracha
from PatoBravo import PatoBravo
from PatoRuivo import PatoRuivo
from VoarFoguete import VoarFoguete

class Main:
 
    @staticmethod
    def run():
        pato = PatoRuivo()		
        print(pato.mostrar())
        print(pato.nadar())
        print(pato.comportamentoPato())
        pato.setComportamento(VoarFoguete())
        print(pato.comportamentoPato())


Main().run()
