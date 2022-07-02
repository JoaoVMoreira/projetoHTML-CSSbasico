import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolTip, QLineEdit
import random

numero_sorteado = 0
contador = 0

class JogoDoChute(QMainWindow):
    def __init__(self):
        super().__init__()

        #Jogo do chute
        titulo = QLabel(self)
        titulo.setText('Jogo do chute!')
        titulo.move(450, 40)
        titulo.resize(300, 40)
        titulo.setStyleSheet('QLabel {font-size: 35px; font: bold; color: green}')

        #botao sortear
        botao_sortear = QPushButton('Sortear', self)
        botao_sortear.move(500, 120)
        botao_sortear.resize(180, 80)
        botao_sortear.setStyleSheet('QPushButton {background-color: red; font-size: 25px; font: bold; color: white}')
        botao_sortear.clicked.connect(self.botaoSortear)

        #Insira seu chute
        insira_chute = QLabel(self)
        insira_chute.setText('Insira seu chute:')
        insira_chute.move(300, 250)
        insira_chute.resize(300, 40)
        insira_chute.setStyleSheet('QLabel {font-size: 20px; font: bold}')

        #Gerando botão verificar
        verificar = QPushButton('Verificar', self)
        verificar.move(650, 250)
        verificar.resize(180, 90)
        verificar.setStyleSheet('QPushButton {background-color: green; font-size: 25px; font: bold; color: white}')
        verificar.clicked.connect(self.botaoVerificar)

        # chute 
        self.chute = QLineEdit(self)
        self.chute.move(310, 300)
        self.chute.resize(150, 25)

        #numero sorteado
        self.numero_sorted = QLabel(self)
        self.numero_sorted.move(100, 100)
        self.numero_sorted.resize(300, 25)
        self.numero_sorted.setStyleSheet('QLabel {font-size: 20px; font: bold; color: blue}')

        #resultado
        self.resultado = QLabel(self)
        self.resultado.move(390, 450)
        self.resultado.resize(600, 48)


        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(100, 70, 1200, 650)
        self.setWindowTitle('Jogo do Chute')
        self.show()
    
    def botaoSortear(self):
        self.numero_sorteado = int(random.randint(0, 500))
        self.numero_sorted.setText('Numero sorteado!')


    def botaoVerificar(self):
        
        conteudo = int(self.chute.text())
        
        if conteudo == self.numero_sorteado:
            self.resultado.setText('Você acertou')
            self.resultado.setStyleSheet('QLabel {font-size: 45px; font: bold; color: green}')
        elif conteudo < self.numero_sorteado:
            self.resultado.setText('Tente um numero maior')
            self.resultado.setStyleSheet('QLabel {font-size: 45px; font: bold; color: red}')
        elif conteudo > self.numero_sorteado:
            self.resultado.setText('Tente um numero menor')
            self.resultado.setStyleSheet('QLabel {font-size: 45px; font: bold; color: red}')


aplicacao = QApplication(sys.argv)
j = JogoDoChute()
sys.exit(aplicacao.exec_())