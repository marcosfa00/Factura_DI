from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# por cupuesto lo primero es crear un canva
canvas = canvas.Canvas('tiposDeLetra.pdf', pagesize=A4)# Tamaño máximo de un A4 es: 595 x 842 puntos

# creamos una frase que queramos escribir
frases = []
frases.append("como me gusta el arroz con huevos")

# creamos el objecto writter+

writter = canvas.beginText()
writter.setTextOrigin(25,421)# marcamos la x y
writter.setFont("Helvetica", 14)
writter.setFillColorRGB(1, 0, 1)#rgb 0 o 1
# vamos a recorrer todas las letras y escribir una frase de un tipo de letra diferente
cursor = 0
for letra in canvas.getAvailableFonts():
    writter.setCharSpace(0)# seteamos el espacio entre caracteres
    writter.setFont(letra, 14)
    writter.textLine(letra + "tipo letra")
    #ahora debemos movel el cursor para que no se sobrepongan las leteras
    #ah pues no no pasa eso, ya que el textLine pone un salto de linea al final, pero con el cursor podemos mover la posicion de las letras ej
    writter.moveCursor(cursor -20, cursor + 40)




canvas.drawText(writter)
canvas.save()

