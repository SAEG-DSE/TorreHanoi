class Hanoi():
    def __init__(self):
        self.pino1= ["A", "B", "C","D","E","F","G"]
        self.pino2=[]
        self.pino3=[]
        self.tabuleiro=[self.pino1, self.pino2, self.pino3]

    def movimentar(self,pino_origem,pino_destino):
        origem = self.tabuleiro[pino_origem-1]
        destino = self.tabuleiro[pino_destino-1]
        if (len(origem) == 0):
            raise Exception ("Retirada de peca de pino vazio")
        if(len(destino) > 0 and origem[0] > destino[-1]):
            raise Exception("Peca maior sobre a menor")
        destino.append(origem.pop(0))
