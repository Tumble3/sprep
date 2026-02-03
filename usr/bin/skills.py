from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = A4
c = canvas.Canvas("skills_section.pdf", pagesize=A4)

margin_x = 40
start_y = PAGE_HEIGHT - 100
row_height = 18

# Column positions
skill_x = margin_x
circle_x = skill_x + 200
value_x = circle_x + 120

def draw_skill(y, name, attributes):
    c.drawString(skill_x, y, name)

    x = circle_x
    for attr in attributes:
        c.circle(x, y + 4, 5)
        c.drawString(x + 10, y, attr)
        x += 45

    c.rect(value_x, y - 2, 40, 14)

def draw_group_title(y, title):
    c.setFont("Helvetica-Bold", 11)
    c.drawString(skill_x, y, title)
    c.setFont("Helvetica", 10)

# Section title
c.setFont("Helvetica-Bold", 12)
c.drawString(skill_x, start_y + 25, "Skills")

c.setFont("Helvetica", 10)

draw_group_title(start_y, "Example")

draw_skill(start_y, "Acrobatics", ["AGI"])
draw_skill(start_y - row_height, "Stealth", ["AGI", "TEC"])
draw_skill(start_y - row_height * 2, "Survival", ["STR", "TEC", "INT"])

c.showPage()
c.save()
