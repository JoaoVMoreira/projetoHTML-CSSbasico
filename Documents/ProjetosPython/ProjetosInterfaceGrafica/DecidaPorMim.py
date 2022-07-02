import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
import random

possiveis_respostas = ['Sim', 'Claro', 'Com certeza', 'Ta esperando oque?', 'Não', 'De jeito nenhum', 'claro que não', 'Nunca', 'Faz oque quiser', 'Talvez', 'Pode ser, vai']

class DecidaPorMim(QMainWindow):
    def __init__(self):
        super().__init__()

        #Qual a sua pergunta?
        qual_pergunta = QLabel(self)
        qual_pergunta.setText('Qual a sua pergunta?')
        qual_pergunta.move(135, 100)
        qual_pergunta.setStyleSheet('QLabel {font-size: 30px; font: bold}')
        qual_pergunta.resize(350, 35)

        #input pergunta
        self.pergunta = QLineEdit(self)
        self.pergunta.move(125, 160)
        self.pergunta.resize(350, 45)

        #botão enviar
        enviar = QPushButton('Enviar', self)
        enviar.move(125, 220)
        enviar.resize(170, 50)
        enviar.setStyleSheet('QPushButton {background-color: green; font-size: 20px; font: bold; color: white}')
        enviar.clicked.connect(self.Botao1Clicado)

        #botao gerar
        gerar = QPushButton('Gerar', self)
        gerar.move(300, 220)
        gerar.resize(170, 50)
        gerar.setStyleSheet('QPushButton {background-color: red; font-size: 20px; font: bold; color: white}')
        gerar.clicked.connect(self.Botao2Clicado)

        #Mostrar pergunta
        self.mostra_pergunta = QLabel(self)
        self.mostra_pergunta.move(125, 280)
        self.mostra_pergunta.resize(400, 35)
        self.mostra_pergunta.setStyleSheet('QLabel {font-size: 25px; font: bold}')

        #mostrar resposta
        self.mostrar_resposta = QLabel(self)
        self.mostrar_resposta.move(125, 350)
        self.mostrar_resposta.resize(400, 35)
        self.mostrar_resposta.setStyleSheet('QLabel {font-size: 25px; font: bold; color: blue}')

        self.CarregaJanela()
    
    def CarregaJanela(self):
        self.setGeometry(430, 100, 600, 600)
        self.setWindowTitle('Decida por mim')
        self.show()

    def Botao1Clicado(self):
        texto = self.pergunta.text()
        self.mostra_pergunta.setText(texto)

    def Botao2Clicado(self):
        resposta_final = possiveis_respostas[random.randint(0, 10)]
        self.mostrar_resposta.setText(resposta_final)


aplicacao = QApplication(sys.argv)
d = DecidaPorMim()
sys.exit(aplicacao.exec_())