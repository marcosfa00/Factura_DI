import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QPushButton, QComboBox, QLineEdit,
                             QGroupBox, QTableView)

from conexionBD import ConexionBD
from modeloTaboa import ModeloTaboa
from Factura import Factura


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.codigoProducto =0
        self.nAlbaran= 0
        self.cantidade = 0
        self.precioUnitario =0
        self.numeroLalbaran =0

        self.selected_data = []



        self.setWindowTitle("Exame 20-02-2024")

        # Conexión a la base de datos
        self.obxConeccionBD = ConexionBD("modelosClasicos.dat")
        self.obxConeccionBD.conectaBD()
        self.obxConeccionBD.creaCursor()


        gpbAlbara = QGroupBox("Albará")


        lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblDataEntrega = QLabel("Data entrega")
        lblNumeroCliente = QLabel("Número cliente")

        self.cmbNumeroAlbara = QComboBox()
        # cargar los datos en el combo
        datosCombo = self.obxConeccionBD.consultaSenParametros("SELECT numeroAlbaran FROM ventas")
        for fila in datosCombo:
            self.cmbNumeroAlbara.addItem(str(fila[0]))
        self.cmbNumeroAlbara.currentIndexChanged.connect(self.cambiarDatosAlbara)

        self.txtDataAlbara = QLineEdit()
        self.txtDataEntrega = QLineEdit()
        self.txtNumeroCliente = QLineEdit()

        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.on_btnBorrar_clicked)
        btnImprimir = QPushButton("Imprimir")
        btnImprimir.clicked.connect(lambda: self.crearFactura("FACTURA PROFORMA",self.cmbNumeroAlbara.currentText(),self.txtDataAlbara.text(),self.txtDataEntrega.text(),self.txtNumeroCliente.text()))

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # caja horizontal que contiene toda la ventana
        cajaV = QVBoxLayout()

        # grid que contiene el albará
        gridAlbara = QGridLayout()
        gridAlbara.addWidget(lblNumeroAlbara,0,0)
        gridAlbara.addWidget(self.cmbNumeroAlbara,0,1)
        gridAlbara.addWidget(lblDataAlbara,0,2)
        gridAlbara.addWidget(self.txtDataAlbara,0,3)
        gridAlbara.addWidget(lblDataEntrega,1,0)
        gridAlbara.addWidget(self.txtDataEntrega,1,1,1,3)
        gridAlbara.addWidget(lblNumeroCliente,2,0)
        gridAlbara.addWidget(self.txtNumeroCliente,2,1,1,3)

        gpbAlbara.setLayout(gridAlbara)
        cajaV.addWidget(gpbAlbara)

        # caja vertical que contiene los botones
        cajaH = QHBoxLayout()
        cajaH.addWidget(btnEngadir)
        cajaH.addWidget(btnEditar)
        cajaH.addWidget(btnBorrar)
        cajaH.addWidget(btnImprimir)


        cajaV.addLayout(cajaH)

        # creación de la tabla
        self.tablaDetalleAlbara = QTableView()
        # cambiar el seleccionar fila
        # to select the entire row
        self.tablaDetalleAlbara.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # to select only one row
        self.tablaDetalleAlbara.setSelectionMode(QTableView.SelectionMode.MultiSelection)#cambiamos sigle selection por multi selection


        # implementacion medida de usuabilidade
        self.headerData = self.obtenerNombreColumnas()

        cajaV.addWidget(self.tablaDetalleAlbara)

        # Creación de la caja horizontal que contiene los botones aceptar y cancelar
        cajaAC = QHBoxLayout()
        cajaAC.addWidget(btnCancelar)
        cajaAC.addWidget(btnAceptar)

        # añadir la caja horizontal a la caja vertical al final
        cajaV.addLayout(cajaAC)

        # Contenedor principal
        container = QWidget()
        container.setLayout(cajaV)

        self.cambiarDatosAlbara()

        # to do the selection
        self.selection = self.tablaDetalleAlbara.selectionModel()
        self.selection.selectionChanged.connect(self.on_row_selected)

        self.setCentralWidget(container)
        self.setFixedSize(512, 500)

        self.show()

    # metodo cambiar numero albará
    def cambiarDatosAlbara(self):
        numeroAlbara = self.cmbNumeroAlbara.currentText()
        datosAlbara = self.obxConeccionBD.consultaConParametros("SELECT * FROM ventas WHERE numeroAlbaran=?", numeroAlbara)
        self.txtDataAlbara.setText(datosAlbara[0][1])
        self.txtDataEntrega.setText(datosAlbara[0][2])
        self.txtNumeroCliente.setText(str(datosAlbara[0][3]))
        self.changeTableData(numeroAlbara)

    # metodo cambiar datos de la tabla
    def changeTableData(self, numeroAlbara):
        self.tableData = self.obxConeccionBD.consultaConParametros("SELECT * FROM main.detalleVentas WHERE numeroAlbaran=?", numeroAlbara)
        modelo = ModeloTaboa(self.tableData, self.headerData)
        self.tablaDetalleAlbara.setModel(modelo)

        # cambiar el tamaño de las columnas dependiendo del tamaño del contenido
        self.tablaDetalleAlbara.resizeColumnsToContents()

    # metodo para borrar la fila seleccionada
    def on_btnBorrar_clicked(self):
        index = self.tablaDetalleAlbara.selectedIndexes()
        if not index==[]:
            numeroAlbara = self.tableData[index[0].row()][0]
            codigoProducto = self.tableData[index[0].row()][1]
            isDeleted = self.obxConeccionBD.consultaParaBorrado("DELETE FROM main.detalleVentas WHERE numeroAlbaran=? AND codigoProducto=?", numeroAlbara, codigoProducto)
            if isDeleted:
                self.tableData.pop(index[0].row())
                self.obxConeccionBD.conexion.commit()
                self.changeTableData(numeroAlbara)
            else:
                print("Error al borrar la fila")


    # metodo para obtener el nombre de las columnas
    def obtenerNombreColumnas(self):
        resultado = self.obxConeccionBD.consultaSenParametros("PRAGMA table_info(detalleVentas)")
        nombres_columnas = [columna[1] for columna in resultado]
        return nombres_columnas

    def on_row_selected(self):

        """
          if not index==[]:
            self.nAlbaran =self.tableData[index[0].row()][0]
            self.codigoProducto = self.tableData[index[0].row()][1]
            self.cantidade =self.tableData[index[0].row()][2]
            self.precioUnitario = self.tableData[index[0].row()][3]
            print(self.precioUnitario)
            self.numeroLalbaran = self.tableData[index[0].row()][4]
        """

        selected_indexes = self.tablaDetalleAlbara.selectedIndexes()

        selected_rows = set(index.row() for index in selected_indexes)


        for row in selected_rows:
            data = [

                self.tableData[row][0],  # self.nAlbaran
                self.tableData[row][1],  # self.codigoProducto
                self.tableData[row][2],  # self.cantidade
                self.tableData[row][3],  # self.precioUnitario
                self.tableData[row][4]  # self.numeroLalbaran
            ]
            self.selected_data.append(data)




    def crearFactura(self,tituloFactura,nFactura,fecha,fechaEntrega,numeroCliente):
        nombreArchivo ="FacturaExamen.pdf"
        factura = Factura(nombreArchivo,tituloFactura,self.nAlbaran,fecha,fechaEntrega,numeroCliente,self.codigoProducto,self.precioUnitario,"0000","0000", self.tableData)
        print(factura)







if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()
