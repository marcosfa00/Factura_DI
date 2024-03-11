from reportlab.platypus import Flowable
from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


class Factura:
    def __init__(self,cliente ="",ciudad="",CP="",NIF="",NFactura="",Fecha="",NPedido=""):
        self.cliente = cliente
        self.ciudad = ciudad
        self.CP = CP
        self.NIF = NIF
        self.NFactura = NFactura
        self.Fecha = Fecha
        self.NPedido = NPedido


        self.elementosDoc = []
        self.hojaEstilo = getSampleStyleSheet()

        #desde aquí llamaremos a nuestras funciones
        self.title()
        self.datosFacturacion()



        # construimos el documento FACTURA
        documento = SimpleDocTemplate('facturaInterfaz.pdf', pagesize=A4)
        documento.build(self.elementosDoc)

    def title(self):
        logo = Image("Capgemini_Logo.png",width=200,height=60)
        elements = [
            ["FACTURA Proforma", logo]
        ]
        style=[
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("TEXTCOLOR", (0,0),(-1,-1),colors.lightsalmon),
            ("FONTSIZE",(0,0),(-1,-1),20),
            ("ALIGN",(1,0),(-1,0),"RIGHT"),
            ("ALIGN",(0,0),(-2,0),"LEFT"),
            ("VALIGN",(0,0),(-1,-1),"MIDDLE")
        ]
        table = Table(data=elements, style=style)
        self.elementosDoc.append(table)

    def datosFacturacion(self):
        elements = [
            ["FACTURAR A:"," "," Nº de Factura:",self.NFactura],
            ["CLIENTE:",self.cliente ,"Fecha:",self.Fecha],
            ["DOMICILIO:",self.ciudad,"NPedido:",self.NPedido],
            ["CP:",self.CP,"Fecha de vencimiento:","12/03/2024"],
            ["(NIF):",self.NIF],

        ]

        style = [
            ("BACKGROUND",(0,0),(-1,-1),colors.lightgrey),
            # ("GRID",(0,0),(-1,-1),1,colors.black),

        ]
        tabla = Table(data=elements,style=style, colWidths=[100,100,100,100])
        self.elementosDoc.append(tabla)


    def tablaDatosFacturacion(self):
        print("Tabla de datos")







