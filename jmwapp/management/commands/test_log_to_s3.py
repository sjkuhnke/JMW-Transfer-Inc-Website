from django.core.management import BaseCommand
from jmwapp.views import JobApplicationView


class Command(BaseCommand):
    help = "Test logging an error message to S3 without an actual error."

    def handle(self, *args, **options):
        view_instance = JobApplicationView()
        sample_error_message = "This is a test error message to verify S3 logging functionality."
        view_instance.log_error_to_s3(sample_error_message)
        self.stdout.write(self.style.SUCCESS("Successfully logged test error to S3"))
