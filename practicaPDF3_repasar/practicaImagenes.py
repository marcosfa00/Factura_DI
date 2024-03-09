from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

from reportlab.graphics.shapes import Image, Drawing

# Lista que contendrá los objetos Drawing
imagenes = []

# Creamos un objeto de tipo Drawing
drawing = Drawing()

# Tamaño máximo de un A4 es: 595 x 842 puntos
imagen = Image(200, 400, 160, 160, './biologia.png')  # Posición x, posición y, ancho, alto, ruta
drawing.add(imagen)

# Modificación en la imagen: trasladar la imagen 200 puntos hacia la derecha y 200 puntos hacia arriba
#drawing.translate(200, 200)

# Guardamos el objeto Drawing en una lista (nota: deberías añadir "drawing", no "imagen")
imagenes.append(drawing)

# Creamos un nuevo objeto Drawing con el tamaño de una página A4
drawing = Drawing(A4[0], A4[1])

# Añadimos cada objeto Drawing individualmente a la nueva página A4

drawing.add(imagenes[0])

# Creamos el archivo PDF y añadimos el objeto Drawing con la lista de objetos Drawing
renderPDF.drawToFile(drawing, 'imagenes.pdf')
