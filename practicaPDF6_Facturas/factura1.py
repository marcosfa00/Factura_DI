

from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Clase para posicionar la tabla en el docuemnto
class PositionedTable(Flowable):
    def __init__(self, table,x,y):
        Flowable.__init__(self)
        self.table = table
        self.x = x
        self.y = y

        # tras crear el constructor para posicionar una talba al cual le pasamos una tabla y su posicion en X e Y

    def draw(self):
        self.canv.saveState()  # gaurda el estado del lienzo para poder restaurarlo más tarde
        self.canv.translate(self.x, self.y)  # posiciona la tabla con los valores que le hemos indicado a x e y
        self.table.wrapOn(self.canv, 0, 0)  # ajusta el tamaño de la tabla al lienzoPDF
        self.table.drawOn(self.canv, 0, 0)  # dibuja en el Lienzo la tabla
        self.canv.restoreState()  # restaura el estado original del lienzo para poder dibujar mas tablas


class Factura:
    def __init__(self):
        #inicializando estilos y elementos del docuemnto
        self.hojaEstilo = getSampleStyleSheet()
        self.elementosDoc = []

        #elementos necesarios para construir una factura
        #se programarán en funciones a continuacion
        '''
        Se necesita:
        Borde izquierdo
        Cabecera
        tabla superior
        tabla direccion y datos cleinte
        tabla de productos
        total
        lineaSeparadora
        pie de pagina
        '''
        self.bordeIzquierdo()
        self.titulo()
        self.nombre_logo()
        self.direccion_Facturacion()
        self.tablaFacturas()
        self.total()
        self.lineaSeparadora()
        self.piePagina()

        # construimos el documento FACTURA
        documento = SimpleDocTemplate('factura.pdf', pagesize=A4)
        documento.build(self.elementosDoc)

    def piePagina(self):
        pie_estilo = self.hojaEstilo["BodyText"]
        pie_estilo.textColor = colors.darkgreen
        pie_estilo.alignment = 1 # 0 izquierda, 1 centro, 2 derecha
        pie_estilo.fontName = "Helvetica-Bold"

        pie = Paragraph("GRACIAS POR SU CONFIANZA", pie_estilo)
        self.elementosDoc.append(pie)
    def lineaSeparadora(self):
        elementos=[""],
        estilo=[
            ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
        ]
        tabla = Table(data=elementos, style=estilo, colWidths=[490], rowHeights=35)
        self.elementosDoc.append(Spacer(0, 20))
        self.elementosDoc.append(tabla)

    def total(self):
        elementos = [
            ["","","TOTAL",385]
        ]
        estilo= [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # color de la letra
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            # cambiar el fondo
            ("BACKGROUND", (-2, 0), (-1, 0), colors.darkgreen),
            # cambiar el tamaño
            ("FONTSIZE", (0, 0), (-1, -1), 12),
            # poner en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # align hacia el centro
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            # espacio entre celdas
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
        ]
        tabla = Table(data=elementos, style=estilo, colWidths=[210,90,90,100],rowHeights=35)
        self.elementosDoc.append(Spacer(0, 25))
        self.elementosDoc.append(tabla)

    def direccion_Facturacion(self):
        elementos=[
            ["Dirección"],
            ["Ciudad y País"],
            ["CIF/NIF", "Fecha Emisión", "DD/MM/AAAA"],
            ["Teléfono", "Número de Factura", "A0001"],
            ["Mail"]
        ]
        estilo= [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # color de la letra
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.darkgreen),
            # cambiar el tamaño
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            # poner en negrita + cursiva
            ("FONTNAME", (0, 0), (1, -1), "Helvetica-BoldOblique"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia el medio
            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            # align hacia el medio
            ("ALIGN", (2, 0), (-1, -1), "CENTER"),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[300,100,100])
        self.elementosDoc.append(Spacer(0, 30))
        self.elementosDoc.append(tabla)

    def tablaFacturas(self):
        elementos = [
            #titulos
            ["Descripcion","Importe","CAntidad","Total"],
            #datos
            ["Producto 1", "3,2", "5", "16,00"],
            ["Producto 2", "2,1", "3", "6,30"],
            ["Producto 3", "2,9", "76", "220,40"],
            ["Producto 4", "5", "23", "115"],
            ["Producto 5", "4,95", "3", "14,85"],
            ["Producto 6", "6", "2", "12,00"],
        ]

        estilo=[
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # color de la letra
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            # cambiar el fondo
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),
            ("BACKGROUND", (0, 1), (-1, -1), colors.lightgreen),
            # poner en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # align hacia el centro
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
            # espacio entre celdas
            ("GRID", (0, 0), (-1, -1), 1, colors.white),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=[210, 90, 90, 100])
        self.elementosDoc.append(Spacer(0,30))
        self.elementosDoc.append(tabla)

    def nombre_logo(self):
        imagen = Image('./biologia.png', 40,40)

        EstiloTitulo = self.hojaEstilo["Heading4"]
        titulo = Paragraph("Marcos S.L", style=EstiloTitulo)
        cabeceraEmpresa= [
            ["Nombre de la empresa", [imagen,titulo]]
        ]
        estilo = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.darkgreen),
            # cambiar el tamaño
            ("FONTSIZE", (0, 0), (0, -1), 18),
            # cambiar el tamaño de la otra columna
            ("FONTSIZE", (-1, 0), (-1, -1), 14),
            # poner en negrita
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
            # vertical align
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM")
        ]

        tabla = Table(data=cabeceraEmpresa,style=estilo,colWidths=[400,100])
        self.elementosDoc.append(tabla)





    def titulo(self):
        estilo_titulo = self.hojaEstilo["Heading1"]
        estilo_titulo.alignment = 2 # 0 izquierda 1 centro 2 derecha
        estilo_titulo.textColor = colors.darkgreen
        estilo_titulo.fontSize = 16

        titulo = Paragraph("FACTURA SIMPLIFICADA", estilo_titulo)
        self.elementosDoc.append(titulo)

    def bordeIzquierdo(self):
        elementos = [
            [""],
            [""],
            [""],
            [""]
        ]

        estilo = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            # background
            ("BACKGROUND", (0, 0), (0, 0), colors.darkgreen),
            ("BACKGROUND", (0, 1), (0, 1), colors.lightgreen),
            ("BACKGROUND", (0, 2), (0, 2), colors.white),  # para que haya espacio en blanco
            ("BACKGROUND", (0, 3), (0, 3), colors.lightgreen),

        ]

        tablaIzquierda = Table(data=elementos, style=estilo, colWidths=27, rowHeights=[50, 340, 5, 200])
        tabla = PositionedTable(tablaIzquierda, -60, -600)
        self.elementosDoc.append(tabla)







if __name__ == "__main__":
    factura = Factura()
    print("Factura creada")