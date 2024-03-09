from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


# creamos la calse para darle posicion a la tabla
class PositionTable(Flowable):
    def __init__(self, table, x, y):
        self.table = table
        self.x = x
        self.y = y

    def draw(self):
        """
           Dibuja la tabla en el lienzo PDF, aplicando transformaciones de posición.

           Esta función realiza una serie de operaciones para posicionar y dibujar la tabla en el lienzo PDF.

           1. Guarda el estado actual del lienzo para poder restaurarlo más tarde.
           2. Translada la tabla a la posición especificada por los valores de 'x' e 'y'.
           3. Ajusta el tamaño de la tabla al lienzo PDF.
           4. Dibuja la tabla en el lienzo PDF.
           5. Restaura el estado original del lienzo, permitiendo dibujar más tablas si es necesario.

           Nota: Esta función asume que existen atributos de instancia llamados 'canv', 'x', 'y' y 'table'.

           :raises AttributeError: Si alguno de los atributos 'canv', 'x', 'y' o 'table' no está presente en la instancia.
           """
        self.canv.saveState()  # gaurda el estado del lienzo para poder restaurarlo más tarde
        self.canv.translate(self.x, self.y)  # posiciona la tabla con los valores que le hemos indicado a x e y
        self.table.wrapOn(self.canv, 0, 0)  # ajusta el tamaño de la tabla al lienzoPDF
        self.table.drawOn(self.canv, 0, 0)  # dibuja en el Lienzo la tabla
        self.canv.restoreState()  # restaura el estado original del lienzo para poder dibujar mas tablas


class Factura2:
    def __init__(self):
        # declaramos una hoja de estilos para la tabla
        self.hojaEstilo = getSampleStyleSheet()
        # declaramos un array de elementos que será donde añadiremos todos los elementos a ala tabla
        self.elementosDoc = []

        # A continuación llamaremos a todas nuestras funciones para crear la factura
        self.Titulo()
        self.datosFacturacion()
        self.tablaPedidos()

        # construimos el documento FACTURA
        self.documento = SimpleDocTemplate('factura2.pdf', pagesize=A4)
        self.documento.build(self.elementosDoc)
    # Comenzamos con las funciones

    def Titulo(self):
        imagen = Image("./Capgemini_Logo.png", width=150, height=50)
        elementos = [
            ["FACTURA Proforma", imagen]
        ]

        estilo = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("TEXTCOLOR", (0, 0), (0, -1), colors.black),
            ("FONTSIZE", (0, 0), (0, -1), 20),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        ]

        tabla = Table(data=elementos, style=estilo, colWidths=250, rowHeights=50)
        self.elementosDoc.append(tabla)

    def datosFacturacion(self):
        print("Por favor, ingrese los siguientes datos de facturación:")

        # Solicitar datos por consola
        cliente = input("1. Nombre Cliente: ")
        ciudad_pais = input("2. Ciudad y País: ")
        cif_nif = input("3. CIF/NIF: ")
        direccion = input("5. Codigo Postal/Ciudad: ")
        fecha = input("6. Fecha de Factura: ")
        print("Datos de facturación ingresados correctamente.")

        estiloTextos = self.hojaEstilo["BodyText"]

        cliente_text = Paragraph("<b>{}</b>".format(cliente), style=estiloTextos)
        ciudad_pais_text = Paragraph("<b>{}</b>".format(ciudad_pais), style=estiloTextos)
        cif_nif_text = Paragraph("<b>{}</b>".format(cif_nif), style=estiloTextos)
        direccion_text = Paragraph("<b>{}</b>".format(direccion), style=estiloTextos)
        fecha_text = Paragraph("<b>{}</b>".format(fecha), style=estiloTextos)


        elementos = [
            # TITULO DE LA TABLA
            [Paragraph("FACTURAR A:", estiloTextos), "",Paragraph("Nº DE FACTURA", estiloTextos),""],
            # DATOS:
            [Paragraph("Cliente:", estiloTextos), cliente_text,Paragraph("Fecha de Factura:", estiloTextos), fecha_text],
            [Paragraph("Ciudad y País:", estiloTextos), ciudad_pais_text,Paragraph("Nº DE PEDIDO", estiloTextos)],
            [Paragraph("Codigo Postal/Ciudad:", estiloTextos), direccion_text,Paragraph("Fecha de Vencimiento", estiloTextos)],
            [Paragraph("CIF/NIF:", estiloTextos), cif_nif_text,Paragraph("Condiciones de Pago", estiloTextos)],


            # Añade más filas según sea necesario
        ]
        estilo = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),

        ]
        tabla = Table(data=elementos, style=estilo, colWidths=125)
        self.elementosDoc.append(tabla)

    def tablaPedidos(self):
        elementos = [
            #titulo
            ["Pos.","Concepto/Descripción","Cantidad","Unidad","Precio Unitario","Importe"],
            #Datos
            ["1","","","","",""],
            ["2", "", "", "", "", ""],
            ["", "", "", "", "", ""]
        ]

        estilo = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ]
        tabla = Table(data=elementos, style=estilo, colWidths=[50,120,90,90,90,100])
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tabla)





if __name__ == "__main__":
    factura = Factura2()
    print("Factura creada")
