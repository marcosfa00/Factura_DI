#comenzamos creando una tabla

from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.platypus import SimpleDocTemplate, Table, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# lo primero es crear una hoja de estuilos en la cual vamos a situar la tabla

hojaEstiloTabla = getSampleStyleSheet()
# esta tabla va a constar de una imagen y otros titulos diferentes por fila
imagen = Image('biologia.png', 20,50)

estiloCuerpoTexto = hojaEstiloTabla["BodyText"] # obtenemos el estilo de la tabla en un avariable
estiloCuerpoTexto.textColor = Color(0,0,250,0.5) # indicamos el color que va a tener el texto de la tabla
# ahora editamos el estilod el titulo
estiloTitulo = hojaEstiloTabla["Heading1"] # aquí podemos indicar igual que en HTML si es 1,2,3,4,5,6,7,8,9

# creamos un parrafo con el estilo del cuerpo ya que va a ser un capo de la tabla
datoEmpresa1 = Paragraph("Empresa1", style=estiloCuerpoTexto)
empresa1Titulo = Paragraph("Empresa1 Titulo", style=estiloTitulo)

elementosTabla = [] # en este array meteremos los elementos de la tabla

# creamos un array con los datos de la tabla
datosTabla = [
    # cabecera
    ["Empresas", "Candidato1", "Candidato2", "Especificaciones"],

    #datos
    ["CApgemini", "Marcos", "Angel", "Desenvolvemento EDE"],
    [[datoEmpresa1, empresa1Titulo],"JAy","no hay","UNA EMPRESA DE HACER COSAS"],
    [[datoEmpresa1, imagen],"Candidato1", "Candidato2","Esta mierda no hay quien la entienda" ]

]
# vamos a darle un poquito de estilo a esat tabla para que se vea mejor:
estilo =[
    # estilo , (inicio columna, inicio fila), (fin columna, fin fila), color
    #COLOR TEXTO
    ("TEXTCOLOR",(0,0),(0,-1), colors.blue),
    ("TEXTCOLOT",(1,0),(-1,0), colors.red),
    ("TEXTCOLOR",(1,1),(-1,-1), colors.yellowgreen),
    # BORDE EXTERIOR (CELDAS)
    ("BOX",(0,0),(-1,-1), 2,colors.black),
    # BORDE INTERIOR (CELDAS)
    ("INNERGRID",(0,0),(-1,-1),1, colors.gray),
    # ALINEAR ELEMENTOS TABLA (IZQUIERDA,MEDIO,DERECHA
    ("VALIGN",(0,0), (-1,-1),"MIDDLE"),


]

# ahora que tenemso los datos de la tabla creados hay que crear el estilo que va a tener la tabla
tabla =Table(datosTabla, style=estilo)

# añadimos a nuestro array de Elementos la tabla
elementosTabla.append(tabla)

documento = SimpleDocTemplate("ejemploTabla.pdf", pagesize = A4, showBoundary = 0)
documento.build(elementosTabla)



