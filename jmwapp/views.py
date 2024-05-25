from django.shortcuts import render, redirect
from .forms import JobApplicationForm

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


def job_application_view(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_success')
    else:
        form = JobApplicationForm()
    return render(request, 'job_application.html', {'form': form})
