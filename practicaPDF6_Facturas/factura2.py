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
        self.metodoDePAgo()
        self.Gracias()

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
        self.elementosDoc.append(Spacer(0, 40))

    def datosFacturacion(self):
        print("Por favor, ingrese los siguientes datos de facturación:")

        # Solicitar datos por consola
        cliente = input("1. Nombre Cliente: ")
        ciudad_pais = input("2. Ciudad y País: ")
        cif_nif = input("3. CIF/NIF: ")
        direccion = input("5. Codigo Postal/Ciudad: ")
        fecha = input("6. Fecha de Factura: ")
        print("Datos de facturación ingresados correctamente.")
        elementos = [
            ["FACTURAR A:", "", "Nº DE FACTURA", ""],
            ["Cliente:", cliente, "Fecha de Factura:", fecha],
            ["Ciudad y País:", ciudad_pais, "Nº DE PEDIDO", ""],
            ["Codigo Postal/Ciudad:", direccion, "Fecha de Vencimiento", ""],
            ["CIF/NIF:", cif_nif, "Condiciones de Pago", ""],
        ]


        estilo = [
            # Color de la letra (inicio columna, inicio fila), (fin columna, fin fila), color
            ("BACKGROUND", (0, 0), (-1, -1), colors.lightgrey),
            ("FONTSIZE",(3,0),(-2,0),18)

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
        tabla = Table(data=elementos, style=estilo, colWidths=[50,135,70,70,70,100])
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tabla)


    def metodoDePAgo(self):
        elementos_tablaPago = [
            ["Métodos de pago:",""],
        ]

        estilo_tablaPago = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("BOX", (0, 0), (-1, -1), 1, colors.black),

            ("VALIGN", (0, 0), (-1, -1), "TOP")

        ]
        tabla1 = Table(data=elementos_tablaPago, style=estilo_tablaPago, colWidths=100, rowHeights=80)

        elementos_TablaImporte = [
            ["importe neto",""],
            ["IVA%",""],
            ["IRPF%",""],
            ["IMPORTE BRUTO",""],
        ]

        estilo_TablaImporte = [
            # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 1, colors.lightgrey),
            ("BACKGROUND",(0,3),(-1,-1),colors.lightgrey),
            # vertical align
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")


        ]

        tabla2 = Table(data=elementos_TablaImporte, style=estilo_TablaImporte, colWidths=[100,50], rowHeights=[20,20,20,40])

        elementos = [
            [tabla1,"",tabla2]
        ]

        estilo= [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            # align hacia la izquierda
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
        ]
        tablaFinal = Table(data=elementos, style=estilo, colWidths=[100,300,100])
        self.elementosDoc.append(Spacer(0, 40))
        self.elementosDoc.append(tablaFinal)


    def Gracias(self):
        elementos_Gracias = [
            ["Gracias por su confianza.",""],
            ["Atentamente,",""]
        ]

        estilo = [
            # align hacia la derecha
            ("ALIGN", (-1, 0), (-1, -1), "LEFT"),

        ]
        table = Table(data=elementos_Gracias, style=estilo, colWidths=[200,300], rowHeights=50)
        self.elementosDoc.append(table)







if __name__ == "__main__":
    factura = Factura2()
    print("Factura creada")

