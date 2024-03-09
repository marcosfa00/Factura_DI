

from reportlab.graphics.charts.barcharts import VerticalBarChart

from reportlab.graphics.shapes import Drawing

from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate

from reportlab.lib.pagesizes import A4



#creamos el array de elementos de la grafica

elementosGrafica = []

#nuestra gráfica va a ser de temperaturas en el año
temperaturas = [
    ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [-3, -4, 2, 5, 9, 1, 11, 12, 3, 4, 5, -10]
]
# Tamaño máximo de un A4 es: 595 x 842 puntos
grafica = Drawing(400,200)# aquí le podemos indicar el tamaño total de la gráica

# va a ser una grafica de barras verticales
barra = VerticalBarChart() #horizontales HorizontalBarChar
#vamos a posicionar la barra en la grafica
barra.x = 50 #empieza en el 50 de 400
barra.y = 50 # empieza en el 50 de 200
#ahora indicamos e tamaño que ocupa
barra.height = 125
barra.width = 300
# ahora le damos los valores a las barras, por lo que nos tenemos que saltar los nombres
barra.data = temperaturas[1:] #así nos saltamos el primer array de nombres
#indicamos el color de la linea exterior de las barras (lo que lo rodea)
barra.strokeColor = colors.black
# indicamos el valor máximo y minimo al que podría llegar la barra
barra.valueAxis.valueMin = -20
barra.valueAxis.valueMax = 30
barra.valueAxis.valueStep = 5 # indica el salto de valores , la linea izquierda vertical
barra.categoryAxis.labels.boxAnchor = 'ne'
barra.categoryAxis.labels.dx = 8 # desplaza el label del titulo 8 casillas a la derecha
barra.categoryAxis.labels.dy = -30 # desplaza el label titulo 30 casillas hacia abajo
barra.categoryAxis.labels.angle = 30 # le damos un angulo de 30 grados de inclinación
barra.categoryAxis.categoryNames = temperaturas[0] #indicamos los nombres de la barra inferior (los meses)
barra.groupSpacing = 5 # espacio entre los GRUPOS de barras (se separan de 10 en 10 puntos)
barra.barSpacing = 2 # separacion entre barras indiciduales

#añadimos nuestra barra a la grafica
grafica.add(barra)

#añadimos a nuestro array de elementos  nuestra frafica
elementosGrafica.append(grafica)

documento = SimpleDocTemplate("exemploGraficaDeBarras.pdf", pagesize = A4)
documento.build(elementosGrafica)



