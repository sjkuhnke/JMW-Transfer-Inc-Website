from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
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
        files_data = request.FILES

        filled_pdf = fill_pdf(form_data)
        print(filled_pdf)
        email = EmailMessage(
            'New Job Application',
            'A new job application has been submitted.',
            'fromtest@test.com',
            ['shaejk29@gmail.com'],
        )
        email.attach('application.pdf', filled_pdf, 'application/pdf')
        email.send()

        return JsonResponse({'success': True})


def download_application(request):
    return render(request, 'download_application.html')
