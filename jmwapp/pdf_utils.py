from datetime import datetime
import os.path

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from io import BytesIO

from jmwWebsite import settings


def fill_pdf(form_data):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    existing_pdf_path = os.path.join(base_dir, 'jmwapp', 'static', 'pdf', 'JMW_Application.PDF')
    buffer = BytesIO()
    pagesize = (816.0, 1056.0)
    c = canvas.Canvas(buffer, pagesize=pagesize)
    font_path = os.path.join(base_dir, 'jmwapp', 'static', 'fonts', 'Pacifico-Regular.ttf')
    pdfmetrics.registerFont(TTFont('Pacifico', font_path))

    c.setFont("Helvetica", 12)

    # -- Section 1 -- #
    first_last = form_data['applicant_name']
    draw_string(c, 110, 690, first_last)
    draw_string(c, 475, 688, format_date(form_data['date_of_application']))
    draw_string(c, 162, 666, 'JMW Transfer, Inc.')
    draw_string(c, 155, 645, 'N2833 Hwy 47')
    draw_string(c, 138, 624, 'Appleton')
    draw_string(c, 342, 622, 'WI')
    draw_string(c, 423, 622, '54913')

    # -- Section 9 -- #
    c.setFont("Pacifico", 14)
    draw_string(c, 100, 289, form_data['signature'])
    draw_string(c, 438, 288, format_date(form_data['date']))

    c.showPage()
    c.setFont("Helvetica", 12)

    # -- Section 2 -- #
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
    time_living = f'{form_data['form-0-time_living']} {form_data['form-0-units']}'
    draw_string(c, 530, 640, time_living)

    # Previous addresses
    for i in range(3):
        address = form_data.get(f'form-{i + 1}-address', '')
        city = form_data.get(f'form-{i + 1}-city', '')
        state = form_data.get(f'form-{i + 1}-state', '')
        zip_code = form_data.get(f'form-{i + 1}-zip', '')
        time_living = f'{form_data.get(f'form-{i + 1}-time_living', '')} {form_data.get(f'form-{i + 1}-units', '')}'

        y_base = 615 - (i * 27)

        draw_string(c, 111, y_base, address)
        draw_string(c, 280, y_base, city)
        draw_string(c, 375, y_base, state)
        draw_string(c, 412, y_base, zip_code)
        draw_string(c, 531, y_base - 1, time_living)

    draw_string(c, 270, 535, handle_yes_no(form_data['legal_right_work']))

    mm, dd, yyyy = split_date(form_data['date_of_birth'])
    draw_string(c, 112, 517, mm)
    draw_string(c, 181, 517, dd)
    draw_string(c, 240, 517, yyyy)
    draw_string(c, 418, 517, handle_yes_no(form_data['proof_of_age']))

    # Worked here before
    worked_here_before = form_data.get('worked_here_before', '')
    draw_string(c, 219, 490, handle_boolean(worked_here_before))
    if worked_here_before == 'on':
        draw_string(c, 100, 473, format_date(form_data.get('worked_here_from', '')))
        draw_string(c, 209, 473, format_date(form_data.get('worked_here_to', '')))
        draw_string(c, 356, 473, f'${form_data.get('rate_of_pay', '')}')
        draw_string(c, 472, 473, form_data.get('previous_position', ''))
        draw_string(c, 127, 455, form_data.get('reason_for_leaving_here', ''))

    currently_employed = form_data.get('currently_employed', '')
    draw_string(c, 140, 436, handle_boolean(currently_employed))
    if currently_employed != 'on':
        draw_string(c, 383, 436, form_data.get('time_since_previously_employed', ''))

    draw_string(c, 123, 418, form_data['who_referred'])
    draw_string(c, 478, 418, f'${form_data['rate_of_pay_expected']}')
    ever_been_bonded = form_data.get('ever_been_bonded', '')
    draw_string(c, 162, 399, handle_boolean(ever_been_bonded))
    if ever_been_bonded == 'on':
        draw_string(c, 499, 399, form_data['name_of_bonding_company'])

    draw_string(c, 49, 340, handle_yes_no(form_data['unable_perform']))
    wrap_text(c, form_data.get('reason_unable_perform'), 552, 47, 303, 18)

    # -- Section 3 -- #
    employment_checkbox = form_data.get('employer_checkbox', '')
    if employment_checkbox != 'on':
        for i in range(6):
            employer_name = form_data.get(f'form-{i}-employer_name', '')
            employer_address = form_data.get(f'form-{i}-employer_address', '')
            employer_city = form_data.get(f'form-{i}-employer_city', '')
            employer_state = form_data.get(f'form-{i}-employer_state', '')
            employer_zip = form_data.get(f'form-{i}-employer_zip', '')
            employer_contact = form_data.get(f'form-{i}-employer_contact', '')
            employer_phone_number = form_data.get(f'form-{i}-employer_phone_number', '')
            subject_to_fmcsr = handle_yes_no(form_data.get(f'form-{i}-subject_to_fmcsr', ''))
            drug_alcohol_testing = handle_yes_no(form_data.get(f'form-{i}-drug_alcohol_testing', ''))
            from_mm, from_dd, from_yyyy = split_date(form_data.get(f'form-{i}-from_employer', ''))
            to_mm, to_dd, to_yyyy = split_date(form_data.get(f'form-{i}-to_employer', ''))
            position_held = form_data.get(f'form-{i}-position_held', '')
            salary_wage = f'${form_data.get(f'form-{i}-salary_wage', '')}'
            reason_for_leaving = form_data.get(f'form-{i}-reason_for_leaving', '')

            if i == 0:
                y_base = 129
                x_offset = 0
            else:
                if i == 1:
                    c.showPage()
                y_base = 733 - ((i - 1) * 130)
                x_offset = 7
                if i > 3:
                    y_base += 2

            c.setFont("Helvetica", 12)
            draw_string(c, 73 - x_offset, y_base, employer_name)
            draw_string(c, 90 - x_offset, y_base - 16, employer_address)
            draw_string(c, 75 - x_offset, y_base - 31, employer_city)
            draw_string(c, 279 - x_offset, y_base - 32, employer_state)
            draw_string(c, 335 - x_offset, y_base - 32, employer_zip)
            draw_string(c, 128 - x_offset, y_base - 48, employer_contact)
            draw_string(c, 365 - x_offset, y_base - 48, employer_phone_number)
            if 0 < i < 3:
                y_base -= 2
            if subject_to_fmcsr == 'Yes':
                draw_string(c, 281 - x_offset, y_base - 62, "\u2713")
            else:
                draw_string(c, 313 - x_offset, y_base - 62, "\u2713")
            if drug_alcohol_testing == 'Yes':
                draw_string(c, 236 - x_offset, y_base - 87, "\u2713")
            else:
                draw_string(c, 268 - x_offset, y_base - 87, "\u2713")
            c.setFont("Helvetica", 9)
            if 0 < i < 3:
                y_base += 2
            if 0 < i < 4:
                y_base -= 2
            elif i >= 4:
                y_base -= 1
            draw_string(c, 468 - x_offset, y_base - 2, from_mm)
            draw_string(c, 500 - x_offset, y_base - 2, f'\'{from_yyyy[2:]}')
            draw_string(c, 533 - x_offset, y_base - 2, to_mm)
            draw_string(c, 566 - x_offset, y_base - 2, f'\'{to_yyyy[2:]}')
            draw_string(c, 503 - x_offset, y_base - 18, position_held)
            draw_string(c, 502 - x_offset, y_base - 33, salary_wage)
            draw_string(c, 454 - x_offset, y_base - 49, reason_for_leaving)
    else:
        c.showPage()

    c.showPage()
    c.setFont("Helvetica", 12)

    # -- Section 4 -- #
    accident_checkbox = form_data.get('accident_checkbox', '')
    if accident_checkbox != 'on':
        for i in range(3):
            accident_date = format_date(form_data.get(f'form-{i}-accident_date', ''))
            accident_nature = form_data.get(f'form-{i}-accident_nature', '')
            accident_fatalities = handle_yes_no(form_data.get(f'form-{i}-accident_fatalities', ''))
            accident_injuries = handle_yes_no(form_data.get(f'form-{i}-accident_injuries', ''))
            accident_spill = handle_yes_no(form_data.get(f'form-{i}-accident_spill', ''))

            y_base = 731 - i * 16

            c.setFont("Helvetica", 10)
            draw_string(c, 120, y_base, accident_date)
            c.setFont("Helvetica", 12)
            draw_string(c, 200, y_base, accident_nature)
            draw_string(c, 359, y_base, accident_fatalities)
            draw_string(c, 441, y_base, accident_injuries)
            draw_string(c, 520, y_base, accident_spill)
    else:
        c.setFont("Helvetica", 20)
        draw_string(c, 295, 717, 'NONE')
        c.setFont("Helvetica", 12)

    # -- Section 5 -- #
    conviction_checkbox = form_data.get('conviction_checkbox', '')
    if conviction_checkbox != 'on':
        for i in range(3):
            conviction_location = form_data.get(f'form-{i}-conviction_location', '')
            conviction_date = format_date(form_data.get(f'form-{i}-conviction_date', ''))
            conviction_charge = form_data.get(f'form-{i}-conviction_charge', '')
            conviction_penalty = form_data.get(f'form-{i}-conviction_penalty', '')

            y_base = 652 - i * 14

            draw_string(c, 51, y_base, conviction_location)
            draw_string(c, 260, y_base, conviction_date)
            draw_string(c, 330, y_base, conviction_charge)
            draw_string(c, 436, y_base, conviction_penalty)
    else:
        c.setFont("Helvetica", 20)
        draw_string(c, 295, 640, 'NONE')
        c.setFont("Helvetica", 12)

    # -- Section 6 -- #
    license_checkbox = form_data.get('license_checkbox', '')
    if license_checkbox != 'on':
        for i in range(4):
            license_state = form_data.get(f'form-{i}-license_state', '')
            license_number = form_data.get(f'form-{i}-license_number', '')
            license_class = form_data.get(f'form-{i}-license_class', '')
            license_endorsements = form_data.get(f'form-{i}-license_endorsements', '')
            license_expiration_date = format_date(form_data.get(f'form-{i}-license_expiration_date', ''))

            y_base = 563 - i * 16

            draw_string(c, 120, y_base, license_state)
            draw_string(c, 166, y_base, license_number)
            draw_string(c, 285, y_base, license_class)
            draw_string(c, 325, y_base, license_endorsements)
            draw_string(c, 494, y_base, license_expiration_date)

    denied_license = handle_yes_no(form_data.get('denied_license', ''))
    suspended_license = handle_yes_no(form_data.get('suspended_license', ''))
    if denied_license == 'Yes':
        draw_string(c, 481, 502, "\u2713")
    else:
        draw_string(c, 553, 502, "\u2713")
    if suspended_license == 'Yes':
        draw_string(c, 481, 490, "\u2713")
    else:
        draw_string(c, 553, 490, "\u2713")
    wrap_text(c, form_data.get('license_details', ''), 300, 291, 477, 13, 62)

    # -- Section 7 -- #
    equipment = [
        'straight_truck',
        'tractor_semi_trailer',
        'tractor_two_trailers',
        'tractor_three_trailers',
        'motorcoach_eight',
        'motorcoach_fifteen'
    ]
    choices = [
        ('van', 287, 10),
        ('tank', 306, 12),
        ('flat', 327, 11),
        ('dump', 349, 13),
        ('refer', 373, 14)
    ]
    y_base = 401
    for i in range(6):
        y = y_base - i * 14
        e = handle_boolean(form_data.get(equipment[i], ''))
        if e == 'Yes':
            draw_string(c, 176, y, "\u2713")
            c.setFont("Helvetica", 9)
            draw_string(c, 393, y, format_date(form_data.get(f'{equipment[i]}_from', '')))
            draw_string(c, 442, y, format_date(form_data.get(f'{equipment[i]}_to', '')))
            c.setFont("Helvetica", 12)
            draw_string(c, 491, y, form_data.get(f'{equipment[i]}_miles', ''))
            if i < 4:
                selection = form_data.get(f'{equipment[i]}_type', '')
                for choice, x, r in choices:
                    if choice == selection:
                        h = r / 2
                        x1 = x - r
                        y1 = y + h + 2
                        x2 = x + r
                        y2 = y - h + 2
                        c.ellipse(x1, y1, x2, y2)
                        break
        else:
            draw_string(c, 206, y, "\u2713")

    draw_string(c, 85, 316, form_data.get('other_name', ''))
    draw_string(c, 279, 316, form_data.get('other_type', ''))
    c.setFont("Helvetica", 9)
    draw_string(c, 393, 316, format_date(form_data.get('other_from', '')))
    draw_string(c, 442, 316, format_date(form_data.get('other_to', '')))
    c.setFont("Helvetica", 12)
    draw_string(c, 491, 316, form_data.get('other_miles', ''))

    wrap_text(c, form_data.get('states_operated_in', ''), 332, 248, 297, 13, 49)
    draw_string(c, 348, 271, form_data.get('special_courses', ''))
    draw_string(c, 308, 258, form_data.get('safe_driving_awards', ''))

    # -- Section 8 -- #
    wrap_text(c, form_data.get('trucking_experience', ''), 530, 50, 212, 13)
    wrap_text(c, form_data.get('courses_other', ''), 530, 50, 173, 13)
    draw_string(c, 50, 134, form_data.get('special_equipment', ''))
    grade = int(form_data['highest_grade_completed'])
    xs = [206, 218, 228, 240, 251, 263, 276, 288,
          389, 401, 413, 425,
          502, 515, 528, 541]
    for i in range(16):
        if i + 1 == grade:
            c.circle(xs[i], 105, 6)
            break

    draw_string(c, 179, 91, form_data['last_school_attended_name'])
    draw_string(c, 435, 91, form_data['last_school_attended_city'])
    draw_string(c, 549, 91, form_data['last_school_attended_state'])

    c.setFont("Pacifico", 14)
    draw_string(c, 100, 31, form_data['signature'])
    draw_string(c, 436, 31, format_date(form_data['date']))

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
    if date_str == '':
        return date_str
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%m/%d/%Y')
    return formatted_date


def handle_boolean(param):
    if param == 'on':
        return 'Yes'
    else:
        return 'No'


def handle_yes_no(param):
    return param.capitalize()


def split_date(date_str):
    if date_str:
        date_obj = format_date(date_str)
        mm, dd, yyyy = date_obj.split('/')
        return mm, dd, yyyy
    else:
        return '', '', ''


def wrap_text(c, text, max_px, x, y, dy, base_x=None):
    if text == '':
        return
    lines = []
    if base_x is not None:
        first_line = simpleSplit(text, c._fontname, c._fontsize, max_px)[0]
        lines.append(first_line)

        remaining_text = text[len(first_line):].strip()

        new_max_px = max_px - (base_x - x)

        remaining_lines = simpleSplit(remaining_text, c._fontname, c._fontsize, new_max_px)
        lines.extend(remaining_lines)
    else:
        lines = simpleSplit(text, c._fontname, c._fontsize, max_px)

    first_line = True
    for line in lines:
        if base_x is not None:
            current_x = x if first_line else base_x
        else:
            current_x = x
        c.drawString(current_x, y, line)
        y -= dy
        first_line = False
