from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = A4

c = canvas.Canvas("character_sheet.pdf", pagesize=A4)

margin = 40

# Header
c.rect(margin, PAGE_HEIGHT - 100, PAGE_WIDTH - 2 * margin, 60)
c.drawString(margin + 10, PAGE_HEIGHT - 70, "Character Name:")
c.drawString(margin + 300, PAGE_HEIGHT - 70, "Player:")

# Attributes box
c.rect(margin, PAGE_HEIGHT - 300, 200, 180)
c.drawString(margin + 10, PAGE_HEIGHT - 130, "Attributes")

# Resources box
c.rect(margin + 220, PAGE_HEIGHT - 300, 200, 180)
c.drawString(margin + 230, PAGE_HEIGHT - 130, "Resources")

# Skills box
c.rect(margin, PAGE_HEIGHT - 550, PAGE_WIDTH - 2 * margin, 220)
c.drawString(margin + 10, PAGE_HEIGHT - 330, "Skills")

# Notes box
c.rect(margin, PAGE_HEIGHT - 750, PAGE_WIDTH - 2 * margin, 180)
c.drawString(margin + 10, PAGE_HEIGHT - 580, "Notes")

c.showPage()
c.save()


