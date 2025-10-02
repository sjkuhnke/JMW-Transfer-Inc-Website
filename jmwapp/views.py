import boto3
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.template.loader import render_to_string
from .forms import JobApplicationForm, EmploymentHistoryFormSet, AccidentRecordFormSet, TrafficConvictionFormSet, \
    LicenseFormSet, License2Form, DrivingExperienceForm, ExperienceQualificationsForm, SignatureForm, \
    ApplicableCheckboxesForm, AddressFormset
from .pdf_utils import fill_pdf
import traceback
import logging
import requests
from datetime import datetime
from botocore.exceptions import ClientError


def home(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'home.html', context)


def about_us(request):
    return render(request, 'about_us.html')


def contact(request):
    recaptcha_site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not name or not email or not message:
            return render(request, 'contact.html', {
                'error': 'All fields are required.',
                'recaptcha_site_key': recaptcha_site_key
            })

        recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        recaptcha_data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        recaptcha_result = requests.post(recaptcha_verify_url, data=recaptcha_data)
        recaptcha_result_json = recaptcha_result.json()

        if not recaptcha_result_json['success']:
            return render(request, 'contact.html', {
                'error': 'reCAPTCHA validation failed. Please try again.',
                'recaptcha_site_key': recaptcha_site_key
            })

        subject = 'New Contact Submission'
        body = render_to_string('contact_email.txt', {
            'name': name,
            'email': email,
            'message': message,
        })

        email = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['jake@jmwtransfer.com', 'andy@jmwtransfer.com']
        )

        monitoring_email = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['shaejk29@gmail.com']
        )

        try:
            email.send()
            monitoring_email.send()
            return render(request, 'contact.html', {
                'success': 'Thank you for your message. We will get back to you shortly.',
                'recaptcha_site_key': recaptcha_site_key
            })
        except Exception as e:
            return render(request, 'contact.html', {
                'error': f'An error occurred: {str(e)}',
                'recaptcha_site_key': recaptcha_site_key
            })
    return render(request, 'contact.html', {
        'recaptcha_site_key': recaptcha_site_key
    })


def services(request):
    return render(request, 'services.html')


def jobs(request):
    return render(request, 'jobs.html')


def trailers(request):
    return render(request, 'trailers.html')


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
        try:
            form_data = request.POST

            filled_pdf = fill_pdf(form_data)
            applicant_email = form_data['email_address']
            position_applied_for = form_data['position_applied_for']
            first_name = form_data['first_name']
            last_name = form_data['last_name']
            file_name = f"{last_name},{first_name}_Application.pdf"
            applicant_name = f"{first_name} {last_name}"
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            # Construct log content
            log_content = "Job Application Submission\n"
            log_content += f"Timestamp: {timestamp}\n\n"
            for field, value in form_data.items():
                log_content += f"{field}: {value}\n"

            log_filename = f"{last_name},{first_name}_Application_Log.txt"

            # Email to Jake and Andy
            email = EmailMessage(
                'New Job Application',
                f'A new job application has been submitted.\n\nFrom: {applicant_email}\nPosition: {position_applied_for}',
                settings.DEFAULT_FROM_EMAIL,
                ['jake@jmwtransfer.com', 'andy@jmwtransfer.com'],
            )

            email.attach(file_name, filled_pdf, 'application/pdf')
            email.attach(log_filename, log_content, 'text/plain')
            email.send()

            email_monitoring = EmailMessage(
                'New Job Application (Monitoring Copy)',
                f'A new job application has been submitted.\n\nFrom: {applicant_email}\nPosition: {position_applied_for}',
                settings.DEFAULT_FROM_EMAIL,
                ['shaejk29@gmail.com'],
            )

            email_monitoring.attach(file_name, filled_pdf, 'application/pdf')
            email_monitoring.attach(log_filename, log_content, 'text/plain')
            email_monitoring.send()

            file_path = f'applications/{file_name}'
            file_url = default_storage.save(file_path, ContentFile(filled_pdf))

            self.log_application_data_to_s3(log_content, applicant_name, timestamp)

            file_url = default_storage.url(file_path)
            return JsonResponse({'success': True, 'file_url': file_url})
        except Exception as e:
            error_message = traceback.format_exc()
            self.log_error_to_s3(error_message)
            return JsonResponse({'success': False, 'error': str(e)})

    def log_error_to_s3(self, error_message):
        s3_client = boto3.client(
            's3',
            region_name=settings.AWS_S3_REGION_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        timestamp = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
        log_file_name = f'job_application_errors/{timestamp}_error_log.txt'
        try:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=log_file_name,
                Body=error_message,
            )
        except ClientError as e:
            logging.error("Failed to upload error log to S3: %s", e)

    def log_application_data_to_s3(self, log_content, applicant_name, timestamp):
        s3_client = boto3.client(
            's3',
            region_name=settings.AWS_S3_REGION_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        text_file_name = f'job_application_logs/{timestamp}_{applicant_name}_log.txt'

        try:
            s3_client.put_object(
                Bucket=bucket_name,
                Key=text_file_name,
                Body=log_content,
                ContentType='text/plain',
            )
        except ClientError as e:
            logging.error("Failed to upload log to S3: %s", e)


def download_application(request):
    return render(request, 'download_application.html')


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
