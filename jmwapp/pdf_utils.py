from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


def fill_pdf(form_data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    x = 100
    y = 750

    for key in form_data:
        value = form_data[key]
        print(f"{key}: {value}")

        # Draw the key-value pair onto the PDF
        c.drawString(x, y, f"{key}: {value}")

        # Move down the page for the next key-value pair
        y -= 20
        # If y position is too low, start a new page
        if y < 50:
            c.showPage()
            y = 750

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf
