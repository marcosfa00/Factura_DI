from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class Factura:
    # en el contructor le pasaremos todos los datos necesarios para crear la factura
    def __init__(self,nombreArchivo,tituloFactura ="",nFactura="",fecha="",fechaEntrega="",numeroCliente="",codigoProducto="",precioUnitario=0,numeroLFactura="",cliente="",selectedData = ""):
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
        self.selectedData =selectedData


        self.sampleSheet = getSampleStyleSheet()
        self.elementosDoc = []
        # llamamos a nuestras funciones que construllen la factura
        self.TituloFactura()
        self.datosFacturacion()
        self.mainTable()
        self.Gracias()
        self.metodoDePAgo()

        self.documento = SimpleDocTemplate(nombreArchivo, pagesize=A4)
        self.documento.build(self.elementosDoc)

    def TituloFactura(self):
        logo = Image("Capgemini_Logo.png", width=150, height=50)
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
            #("GRID", (0,0),(-1,-1),1,colors.black)
        ]
        tabla = Table( data=elementsInvoice,style=style, colWidths=100)
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tabla)

    def mainTable(self):

        #  ,self.codigoProducto,self.precioUnitario,"0000","0000")
        total = float(self.precioUnitario) * 21 / 100

        elementsInvoice2 = [
            #Titulo tabla
            ["POS","CONCEPTO/DESCRPICION","CANTIDAD","UNIDAD","PRECIO Unitario","IMPORTE"],
            #datos tabla
            [self.codigoProducto,"Ferrari Testarrosa","","",self.precioUnitario,total],
            [self.codigoProducto,"Ferrari Testarrosa","","",self.precioUnitario,total],
            [self.codigoProducto,"Ferrari Testarrosa","","",self.precioUnitario,total],
        ]
        elementosInvoice = [
            ["POS", "CONCEPTO/DESCRPICION", "CANTIDAD", "UNIDAD", "PRECIO ", "IMPORTE"],

        ]
        self.importe = 0
        self.importeTotal = 0
        # total = float(self.precioUnitario) * 21 / 100
        for elementos in self.selectedData:
            print(elementos)

            array = list(elementos)
            self.importe = float(elementos[3])
            self.importeTotal += self.importe * 21/100
            array.append(self.importe * 21/100)

            elementosInvoice.append(array)


        style = [
            ("GRID", (0, 0), (-1, -1), 1, colors.black)
        ]

        table = Table( data=elementosInvoice,style=style, colWidths=[30,150,60,60,45,55])
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(table)

    def metodoDePAgo(self):
        elementos_tablaPago = [
            ["Métodos de pago:", ""],
        ]

        estilo_tablaPago = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "TOP")

        ]
        tabla1 = Table(data=elementos_tablaPago, style=estilo_tablaPago, colWidths=100, rowHeights=80)
        self.importeNeto = 0
        for elementos in self.selectedData:
            self.importe = float(elementos[3])
            self.importeNeto += self.importe

        self.importeTotal += self.importeTotal *33/100
        self.importeTotal = round(self.importeTotal,2)
        elementos_TablaImporte = [
            ["importe neto", self.importeNeto],
            ["IVA%", "21"],
            ["IRPF%", "33"],
            ["IMPORTE BRUTO", self.importeTotal],
        ]

        estilo_TablaImporte = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.lightgrey),
            ("BACKGROUND", (0, 3), (-1, -1), colors.lightgrey),
            # vertical align
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")

        ]

        tabla2 = Table(data=elementos_TablaImporte, style=estilo_TablaImporte, colWidths=[100, 50],
                       rowHeights=[20, 20, 20, 40])

        elementos = [
            [tabla1, "", tabla2]
        ]

        estilo = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
        ]
        tablaFinal = Table(data=elementos, style=estilo, colWidths=[100, 300, 100])
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tablaFinal)

    def Gracias(self):
        elementos_Gracias = [
            ["Gracias por su confianza.", ""],
            ["Atentamente,", ""]
        ]

        estilo = [
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "LEFT"),

        ]
        table = Table(data=elementos_Gracias, style=estilo, colWidths=[200, 300], rowHeights=50)
        self.elementosDoc.append(table)





