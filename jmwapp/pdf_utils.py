from datetime import datetime
import os.path

from PyPDF2 import PdfReader, PdfWriter
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.pdfgen import canvas
from io import BytesIO


def fill_pdf(form_data):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    existing_pdf_path = os.path.join(base_dir, 'jmwapp', 'static', 'pdf', 'JMW Application.PDF')
    buffer = BytesIO()
    pagesize = (816.0, 1056.0)
    c = canvas.Canvas(buffer, pagesize=pagesize)

    # draw_grid(c, pagesize)

    c.setFont("Helvetica", 12)

    # Section 1
    first_last = form_data['applicant_name']
    draw_string(c, 110, 690, first_last)
    draw_string(c, 475, 688, format_date(form_data['date_of_application']))
    draw_string(c, 162, 666, 'JMW Transfer, Inc.')
    draw_string(c, 155, 645, 'N2833 Hwy 47')
    draw_string(c, 138, 624, 'Appleton')
    draw_string(c, 342, 622, 'WI')
    draw_string(c, 423, 622, '54913')

    # Section 9

    c.showPage()

    draw_grid(c, pagesize)
    c.setFont("Helvetica", 12)

    draw_string(c, 133, 731, form_data['position_applied_for'])
    first_name, last_name = first_last.split(' ')
    middle_initial = form_data['middle_initial']
    draw_string(c, 69, 712, last_name)
    draw_string(c, 240, 712, first_name)
    draw_string(c, 345, 712, middle_initial)
    draw_string(c, 468, 712, form_data['social_security_number'])
    draw_string(c, 111, 668, form_data['form-0-address'])
    draw_string(c, 385, 668, form_data['form-0-city'])
    draw_string(c, 118, 642, form_data['form-0-state'])
    draw_string(c, 266, 642, form_data['form-0-zip'])
    draw_string(c, 379, 641, form_data['phone_number'])
    time_living = form_data['form-0-time_living'] + ' ' + form_data['form-0-units']
    draw_string(c, 530, 640, time_living)

    # Previous addresses
    for i in range(3):
        address = form_data.get(f'form-{i + 1}-address', '')
        city = form_data.get(f'form-{i + 1}-city', '')
        state = form_data.get(f'form-{i + 1}-state', '')
        zip_code = form_data.get(f'form-{i + 1}-zip', '')
        time_living = form_data.get(f'form-{i + 1}-time_living', '') + ' ' + form_data.get(f'form-{i + 1}-units', '')

        y_base = 615 - (i * 27)

        draw_string(c, 111, y_base, address)
        draw_string(c, 280, y_base, city)
        draw_string(c, 375, y_base, state)
        draw_string(c, 412, y_base, zip_code)
        draw_string(c, 531, y_base - 1, time_living)

    draw_string(c, 270, 535, handle_yes_no(form_data['legal_right_work']))

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


def draw_string(c, x, y, string):
    c.drawString(x, y, string)


def draw_grid(c, pagesize):
    width, height = pagesize
    c.setFont("Helvetica", 6)

    # Draw horizontal lines
    for y in range(0, int(height), 10):
        c.drawString(0, y, str(y))
        c.line(0, y, width, y)

    # Draw vertical lines
    for x in range(0, int(width), 10):
        c.drawString(x, 0, str(x))
        c.line(x, 0, x, height)


def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%m/%d/%Y')
    return formatted_date


def handle_boolean(param):
    print(param)
    return param


def handle_yes_no(param):
    return param.capitalize()
