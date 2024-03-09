from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# creamos el canvas
canvas = canvas.Canvas('textos.pdf', pagesize=A4)

# creamos un Array de frases
frases = [
    "Hola, mundo!",
    "Que tal te va al vida",
    "Muy bien y tu?",
    "Hola, mundo!"
]
# como esto es un objecto e texto (Array) ya no vamos a crear un drawString
writter = canvas.beginText() # creamos un objeto writter
#indicamos la posicion en la que vamso a escribir
# tamaño máximo de un A4 es: 595 x 842 puntos
writter.setTextOrigin(250,420)#aprox la mitad
writter.setFont("Courier",14) # indicamos la fuente y el tamaño con el que vamso a escribir

# ahora procedemos a escribir todas las frases de nuestro array
for frase in frases:
    writter.textLine(frase)

canvas.drawText(writter)  # Corregir esta línea
canvas.showPage()
canvas.save()
