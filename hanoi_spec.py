import unittest
from should_dsl import should
from hanoi import Hanoi

class TestInicializacaoDosPinos(unittest.TestCase):
    def setUp(self):
        self.hanoi = Hanoi()

    def test_pino_um(self):
        self.hanoi.pino1 |should| equal_to(["A", "B", "C","D","E","F","G"])

    def test_tabuleiro(self):
        self.hanoi.pino1 |should| equal_to(["A", "B", "C","D","E","F","G"])
        self.hanoi.pino2 |should| equal_to([])
        self.hanoi.pino3 |should| equal_to([])

class TestMovimentacaoDosDiscos(unittest.TestCase):
    def setUp(self):
        self.hanoi = Hanoi()

    def test_movimenta_A_para_pino2(self):
        self.hanoi.movimentar(1,2)
        self.hanoi.pino1 |should| equal_to(["B", "C","D","E","F","G"])
        self.hanoi.pino2 |should| equal_to(["A"])
        self.hanoi.pino3 |should| equal_to([])

    def test_movimenta_A_para_pino3(self):
        self.hanoi.movimentar(1,3)
        self.hanoi.pino1 |should| equal_to(["B", "C","D","E","F","G"])
        self.hanoi.pino2 |should| equal_to([])
        self.hanoi.pino3 |should| equal_to(["A"])

    def test_movimentacao_ilegal_B_sobre_A(self):
        self.hanoi.movimentar(1,2)
        (self.hanoi.movimentar, 1, 2) |should| throw(Exception, message="Peca maior sobre a menor")

    def test_movimentacao_ilegal_retirada_de_peca_de_pino_vazio(self):
        (self.hanoi.movimentar,2,1) |should| throw(Exception, message='Retirada de peca de pino vazio')
