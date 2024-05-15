from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(nombre_archivo):
    # Crear un lienzo para el PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    
    # Definir el título
    titulo = "Ejemplo de PDF con Python"
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 750, titulo)
    
    # Definir el párrafo
    parrafo = "Este es un PDF generado utilizando Python y la biblioteca ReportLab."
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, parrafo)
    
    # Guardar el PDF
    c.save()


# Generar el PDF
generar_pdf("ejemplo.pdf")