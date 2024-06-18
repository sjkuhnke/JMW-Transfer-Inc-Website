import os

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import JobApplicationForm, EmploymentHistoryFormSet, AccidentRecordFormSet, TrafficConvictionFormSet, \
    LicenseFormSet, License2Form, DrivingExperienceForm, ExperienceQualificationsForm, SignatureForm, \
    ApplicableCheckboxesForm, AddressFormset
from .pdf_utils import fill_pdf


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def jobs(request):
    return render(request, 'jobs.html')


def trailer_types(request):
    return render(request, 'trailer_types.html')


class JobApplicationView(View):
    def get(self, request):
        form = JobApplicationForm()
        address_formset = AddressFormset()
        employment_history_formset = EmploymentHistoryFormSet()
        accident_record_formset = AccidentRecordFormSet()
        traffic_conviction_formset = TrafficConvictionFormSet()
        license_formset = LicenseFormSet()
        applicable_form = ApplicableCheckboxesForm()
        license_2_form = License2Form()
        driving_experience_form = DrivingExperienceForm()
        experience_qualifications_form = ExperienceQualificationsForm()
        signature_form = SignatureForm()
        return render(request, 'job_application.html', {
            'form': form,
            'address_formset': address_formset,
            'employment_history_formset': employment_history_formset,
            'accident_record_formset': accident_record_formset,
            'traffic_conviction_formset': traffic_conviction_formset,
            'license_formset': license_formset,
            'applicable_form': applicable_form,
            'license_2_form': license_2_form,
            'driving_experience_form': driving_experience_form,
            'experience_qualifications_form': experience_qualifications_form,
            'signature_form': signature_form
        })

    def post(self, request):
        form_data = request.POST

        filled_pdf = fill_pdf(form_data)
        applicant_email = form_data['email_address']
        email = EmailMessage(
            'New Job Application',
            f'A new job application has been submitted.\n\nFrom: {applicant_email}',
            'itsrainyjupiter@gmail.com',  # change to app@jmwtransfer.com or no-reply@jmwtransfer.com
            ['shaejk29@gmail.com'],  # change to jake@jmwtransfer.com, andy@jmwtransfer.com, and shaejk29@gmail.com
        )
        applicant_name = form_data['applicant_name']

        name_parts = applicant_name.split()
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        file_name = f"{last_name},{first_name}_Application.pdf" if last_name else f"{first_name}_Application.pdf"

        email.attach(file_name, filled_pdf, 'application/pdf')
        email.send()

        file_path = os.path.join('media', 'applications', file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(filled_pdf)

        file_url = f'/media/applications/{file_name}'
        return JsonResponse({'success': True, 'file_url': file_url})


def download_application(request):
    return render(request, 'download_application.html')
