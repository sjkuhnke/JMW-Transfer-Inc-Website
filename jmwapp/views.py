from django.shortcuts import render, redirect
from django.views import View
from .forms import JobApplicationForm, EmploymentHistoryFormSet, AccidentRecordFormSet, TrafficConvictionFormSet, \
    LicenseFormSet
from .models import TrafficConviction, AccidentRecord, EmploymentHistory, License


# Create your views here.


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
        employment_history_formset = EmploymentHistoryFormSet()
        accident_record_formset = AccidentRecordFormSet()
        traffic_conviction_formset = TrafficConvictionFormSet()
        license_formset = LicenseFormSet()
        return render(request, 'job_application.html', {
            'form': form,
            'employment_history_formset': employment_history_formset,
            'accident_record_formset': accident_record_formset,
            'traffic_conviction_formset': traffic_conviction_formset,
            'license_formset': license_formset
        })

    def post(self, request):
        form = JobApplicationForm(request.POST)
        employment_history_formset = EmploymentHistoryFormSet(request.POST)
        accident_record_formset = AccidentRecordFormSet(request.POST)
        traffic_conviction_formset = TrafficConvictionFormSet(request.POST)
        license_formset = LicenseFormSet(request.POST)

        if form.is_valid() and employment_history_formset.is_valid() and accident_record_formset.is_valid() and traffic_conviction_formset.is_valid() and license_formset.is_valid():
            job_application = form.save()
            for form in employment_history_formset:
                employment_history = form.save(commit=False)
                employment_history.job_application = job_application
                employment_history.save()
            for form in accident_record_formset:
                accident_record = form.save(commit=False)
                accident_record.job_application = job_application
                accident_record.save()
            for form in traffic_conviction_formset:
                traffic_conviction = form.save(commit=False)
                traffic_conviction.job_application = job_application
                traffic_conviction.save()
            for form in license_formset:
                license_experience = form.save(commit=False)
                license_experience.job_application = job_application
                license_experience.save()
            return redirect('application_success')

        return render(request, 'job_application.html', {
            'form': form,
            'employment_history_formset': employment_history_formset,
            'accident_record_formset': accident_record_formset,
            'traffic_conviction_formset': traffic_conviction_formset,
            'license_formset': license_formset
        })


def download_application(request):
    return render(request, 'download_application.html')
