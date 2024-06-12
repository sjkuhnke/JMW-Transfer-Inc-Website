import os.path

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


def fill_pdf(form_data):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    existing_pdf_path = os.path.join(base_dir, 'jmwapp', 'static', 'pdf', 'JMW Application.PDF')
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

    buffer.seek(0)

    existing_pdf = PdfReader(existing_pdf_path)
    output_pdf = PdfWriter()

    new_pdf = PdfReader(buffer)

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        if i < len(new_pdf.pages):
            new_page = new_pdf.pages[i]
            page.merge_page(new_page)
        output_pdf.add_page(page)

    output_buffer = BytesIO()
    output_pdf.write(output_buffer)

    pdf = output_buffer.getvalue()
    output_buffer.close()
    buffer.close()

    return pdf
