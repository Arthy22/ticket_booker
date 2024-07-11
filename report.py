import webbrowser
from fpdf import FPDF


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, user, price, seat):
        pdf = FPDF(orientation='L', unit="pt", format="A4")
        pdf.add_page()
        pdf.set_fill_color(255, 36, 50)
        pdf.rect(65, 145, 700, 300, 'F')
        pdf.set_fill_color(255, 255, 0)
        pdf.rect(95, 185, 635, 225, 'F')
        pdf.set_fill_color(255, 36, 50)
        pdf.ellipse(70, 155, 75, 75, 'F')
        pdf.ellipse(675, 355, 75, 75, 'F')
        pdf.ellipse(675, 155, 75, 75, 'F')
        pdf.ellipse(70, 355, 75, 75, 'F')
        pdf.set_line_width(3)
        pdf.set_draw_color(225, 36, 50)
        pdf.dashed_line(530, 185, 530, 410, 25, 10)
        pdf.set_font(family="Times", size=45, style='B')
        pdf.cell(w=0, h=80, txt="Digital Ticket", border=0, align="C", ln=1)
        pdf.set_font(family="Times", size=20, style='B')
        pdf.text(550, 265, "Name:")
        pdf.text(615, 265, user)
        pdf.text(550, 295, "Price:")
        pdf.text(615, 295, str(price))
        pdf.text(550, 325, "Seat number:")
        pdf.text(670, 325, seat)
        pdf.set_font(family="Times", size=55, style='B')
        pdf.text(100, 295, "BLOCKBUSTER")
        pdf.text(175, 345, "CINEMAS")

        pdf.output(self.filename)
        webbrowser.open(self.filename)
