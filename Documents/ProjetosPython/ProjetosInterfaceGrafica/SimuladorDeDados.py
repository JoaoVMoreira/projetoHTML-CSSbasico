# Simulador de dados com Interface gráfica

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui
import random

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        # Posicionamento da janela
        self.topo = 100
        self.lado = 450

        # Dimenções da Janela
        self.altura = 600
        self.largura = 500
        self.titulo = 'Simulador de dados'

        #Criando "SIMULADOR DE DADOS"
        sim_dados = QLabel(self)
        sim_dados.move(120, 50)
        sim_dados.setText('SIMULADOR DE DADOS')
        sim_dados.setStyleSheet('QLabel {font-size: 20px; color: green; font: bold}')
        sim_dados.resize(300, 20)

        #Criando "Valor mínimo:"
        valor_min = QLabel(self)
        valor_min.move(50, 150)
        valor_min.setText('Valor mínimo: ')
        valor_min.resize(300, 20)
        valor_min.setStyleSheet('QLabel {font-size: 14px; color: black; font: bold}')

         #Criando "Valor máximo:"
        valor_max = QLabel(self)
        valor_max.move(50, 200)
        valor_max.setText('Valor máximo: ')
        valor_max.resize(300, 20)
        valor_max.setStyleSheet('QLabel {font-size: 14px; color: black; font: bold}')

        #Criando "Valor sorteado:"
        valor_sort = QLabel(self)
        valor_sort.move(180, 350)
        valor_sort.setText('Valor sorteado: ')
        valor_sort.resize(300, 20)
        valor_sort.setStyleSheet('QLabel {font-size: 14px; color: black; font: bold}')

        #Criando inserir valor minimo
        self.ins_valor_min = QLineEdit(self)
        self.ins_valor_min.move(300, 150)
        self.ins_valor_min.resize(100, 20)

        #Criando Inserir valor máximo
        self.ins_valor_max = QLineEdit(self)
        self.ins_valor_max.move(300, 195)
        self.ins_valor_max.resize(100, 20)

        #Criando botão para gerar numero
        gerar_numero = QPushButton('Gerar número', self)
        gerar_numero.move(180, 260)
        gerar_numero.resize(100, 50)
        gerar_numero.setStyleSheet('QPushButton {background-color: green; font-size: 20; font: bold; color: white}')
        gerar_numero.clicked.connect(self.BotaoClicado)

        #Criando exibidor do numero sorteado
        self.numero_aleatorio = QLabel(self)
        self.numero_aleatorio.move(220, 420)   
        self.numero_aleatorio.resize(300,50)
        self.numero_aleatorio.setStyleSheet('QLabel {font-size: 40px; font: bold}')

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)  
        self.setWindowTitle(self.titulo)
        self.show()

    def BotaoClicado(self):
        conteudo = self.ins_valor_min.text()
        conteudo2 = self.ins_valor_max.text()
        numeroGerado = random.randint(int(conteudo), int(conteudo2))
        self.numero_aleatorio.setText(f'{numeroGerado}')


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())