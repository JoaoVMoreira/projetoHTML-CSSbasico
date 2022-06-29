# Simulador de dados com Interface gráfica

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

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
        valor_sort.move(180, 300)
        valor_sort.setText('Valor sorteado: ')
        valor_sort.resize(300, 20)
        valor_sort.setStyleSheet('QLabel {font-size: 14px; color: black; font: bold}')

        self.CarregaJanela()

    def CarregaJanela(self):
        self.setGeometry(self.lado, self.topo, self.largura, self.altura)  
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())