from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class Factura:
    # en el contructor le pasaremos todos los datos necesarios para crear la factura
    def __init__(self,nombreArchivo,tituloFactura ="",nFactura="",fecha="",fechaEntrega="",numeroCliente="",codigoProducto="",precioUnitario="",numeroLFactura="",cliente=""):
        self.nombreArchivo =nombreArchivo
        self.tituloFactura = tituloFactura
        self.nFactura = nFactura
        self.fecha = fecha
        self.fechaEntrega = fechaEntrega
        self.numeroCliente = numeroCliente
        self.codigoProducto = codigoProducto
        self.precioUnitario = precioUnitario
        self.numeroLFactura = numeroLFactura
        self.cliente = cliente


        self.sampleSheet = getSampleStyleSheet()
        self.elementosDoc = []
        # llamamos a nuestras funciones que construllen la factura
        self.TituloFactura()
        self.datosFacturacion()

        self.documento = SimpleDocTemplate(nombreArchivo, pagesize=A4)
        self.documento.build(self.elementosDoc)

    def TituloFactura(self):
        logo = Image("../Capgemini_Logo.png", width=150, height=50)
        elementsTitle = [
            [self.tituloFactura, logo ]
        ]

        style = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("ALIGN" , (0,0),(1,0),"LEFT"),
            ("ALIGN" , (1,0),(1,0),"RIGHT"),
            ("VALIGN" ,(0,0),(-1,-1),"MIDDLE"),
        ]
        # CREAMOS UNA TABLA CON ESTOS DATOS
        tabla = Table( data=elementsTitle,style=style, colWidths=200 )
        # añadimos esta tabla al documento
        self.elementosDoc.append(tabla)

    def datosFacturacion(self):
        """
            Genera una tabla de datos de facturación y la agrega a la lista de elementos del documento.

            :return: None
        """

        # nombreArchivo,tituloFactura ="",nFactura="",fecha="",fechaEntrega="",numeroCliente="",
        # codigoProducto="",precioUnitario="",numeroLFactura="",cliente=""

        elementsInvoice = [
            ["FACTURAR A: ",self.numeroCliente,"Nº DE FACTURA", self.nFactura],
            ["Cliente:",self.cliente,"Fecha:",self.fecha],
            ["Domicilio:","","Nº de Pedido",self.numeroLFactura]
        ]
        style = [

            ("BACKGROUND" , (0,0),(-1,-1),colors.lightgrey),
            ("GRID", (0,0),(-1,-1),1,colors.black)
        ]
        tabla = Table( data=elementsInvoice,style=style, colWidths=100)
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tabla)

    def mainTable(self):
        elementsInvoice = []




