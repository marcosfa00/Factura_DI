from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# debemos tener instalado ReportLab

# lo primero será tener un camvas donde poder meter todos los elementos

canvas = canvas.Canvas('./practicaPDF1/practicaPosiciones0.pdf', pagesize=A4)# aquí le damos nombre a nuestro pdf

# ahora procedemos a escribir en nuestro pdf
canvas.drawString(0,0,"Hola que tal")# escribe una liena, necesitamos indicarle la posicion x e Y
# x es el eje horizontal asiq ue si quiero movel a la derecha tendré que aumentar el valor de x
#y es el valor vertical asiq tendré que aumentar en y si quiero sbir el texto
canvas.drawString(100,0,"texto movido a la derecha pero en la misma altura")
canvas.drawString(100,100,"texto en la misma posicion que el anterior, pero con una altura de 100 en Y")

# tabien podemos añadir imagenes a nuestro pdf
canvas.drawImage('resources/biologia.png',25,200, 100,100)# indicamos la ruta de la imagen y depsues su posicion en x y, después su tamaño
# en la imagen tanto wigth cono height podemos modificarlo como nos de la gana para ajustar el tamaño, pero devemos tener cuidado de la relación aspectop d ela imagen
# si no nos quedará una imagen estirada
canvas.save()
