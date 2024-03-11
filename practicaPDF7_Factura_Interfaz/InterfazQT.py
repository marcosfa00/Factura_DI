import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox, QTableWidget, QTableView, QLineEdit)
from Factura import Factura


class VentanaTablaSQL(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TABLA SQL')

        main_window = QVBoxLayout()

        parteInputs = QHBoxLayout()



        main_window.addLayout(parteInputs)


        # vamos a creat los lineEditsNecesarios para cumplimentar una factura
        # vamos a crear los lineEdits necesarios para cumplimentar una factura
        inputs = QWidget()
        layoutInputs = QVBoxLayout()

        lbl_Cliente = QLabel('Cliente')
        txtCliente = QLineEdit()

        lbl_Ciudad_Pais = QLabel('Ciudad y Pais')
        txtCiudad_Pais = QLineEdit()

        lblCodigoPostal = QLabel('Codigo Postal/Ciudad:')
        txtCodigoPostal = QLineEdit()


        # Añadir elementos al layout
        layoutInputs.addWidget(lbl_Cliente)
        layoutInputs.addWidget(txtCliente)

        layoutInputs.addWidget(lbl_Ciudad_Pais)
        layoutInputs.addWidget(txtCiudad_Pais)

        layoutInputs.addWidget(lblCodigoPostal)
        layoutInputs.addWidget(txtCodigoPostal)

        # Establecer el layout para el widget
        inputs.setLayout(layoutInputs)

        parteInputs.addWidget(inputs)


        inputs2 = QWidget()
        layoutInputs2 = QVBoxLayout()

        lbl_CIF = QLabel('CIF')
        txtCIF = QLineEdit()

        lbl_NFactura = QLabel('NFactura')
        txtNFactura = QLineEdit()

        lbl_Fecha = QLabel('Fecha')
        txtFecha = QLineEdit()

        lbl_NPedido = QLabel('Nº de Pedido')
        txtNPedido = QLineEdit()

        Imprimir = QPushButton('Imprimir')
        Imprimir.clicked.connect(lambda: self.btnImprimir(txtCliente,txtCiudad_Pais,txtCodigoPostal,txtCIF,txtNFactura,txtFecha,txtNPedido))


        layoutInputs2.addWidget(Imprimir)
        layoutInputs2.addWidget(lbl_CIF)
        layoutInputs2.addWidget(txtCIF)

        layoutInputs2.addWidget(lbl_NFactura)
        layoutInputs2.addWidget(txtNFactura)

        layoutInputs2.addWidget(lbl_Fecha)
        layoutInputs2.addWidget(txtFecha)

        layoutInputs2.addWidget(lbl_NPedido)
        layoutInputs2.addWidget(txtNPedido)

        inputs2.setLayout(layoutInputs2)

        parteInputs.addWidget(inputs2)



        main_window.addLayout(parteInputs)


        # parte Botones




        #mostramos la ventana
        contenedor = QWidget()
        contenedor.setLayout(main_window)
        self.setCentralWidget(contenedor)
        self.setMinimumSize(QSize(500, 300))
        self.show()

    def btnImprimir(self,cliente,ciudad,cp,nif,nFactura,fecha,nPedido):
        # cliente,ciudad,CP,NIF,NFactura,Fecha,NPedido
        factura = Factura(cliente.text(),ciudad.text(),cp.text(),nif.text(),nFactura.text(),fecha.text(),nPedido.text())
        print("factura creada")




if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTablaSQL()
    aplicacion.exec()