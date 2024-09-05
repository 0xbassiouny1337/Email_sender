import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 24)
    c.drawString(100, 750, f"This is {filename}")
    c.save()

def main():
    for i in range(1, 40):
        filename = f"{i}.pdf"
        create_pdf(filename)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()