from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import JobApplication, EmploymentHistory, AccidentRecord, TrafficConviction, License


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'applicant_name', 'date_of_application',  # Section 1
            'position_applied_for', 'social_security_number', 'date_of_birth', 'legal_right_work',
            'proof_of_age', 'worked_here_before', 'worked_here_from', 'worked_here_to',
            'rate_of_pay', 'previous_position', 'reason_for_leaving_here', 'currently_employed',
            'time_since_previously_employed', 'who_referred', 'rate_of_pay_expected', 'ever_been_bonded',
            'name_of_bonding_company', 'unable_perform', 'reason_unable_perform',  # Section 2
            'address', 'city', 'state', 'zip'  # Section 2
        ]


class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'employer_name', 'employer_address', 'employer_city', 'employer_state',
            'employer_zip', 'employer_contact', 'employer_phone_number', 'subject_to_fmcsr',
            'drug_alcohol_testing', 'from_month', 'from_year', 'to_month', 'to_year',
            'position_held', 'salary_wage', 'reason_for_leaving'
        ]


EmploymentHistoryFormSet = formset_factory(EmploymentHistoryForm, extra=1, max_num=5)


class AccidentRecordForm(forms.ModelForm):
    class Meta:
        model = AccidentRecord
        fields = [
            'last_accident_date', 'last_accident_nature', 'last_accident_fatalities', 'last_accident_injuries',
            'last_accident_spill'
        ]


AccidentRecordFormSet = formset_factory(AccidentRecordForm, extra=1, max_num=3)


class TrafficConvictionForm(forms.ModelForm):
    class Meta:
        model = TrafficConviction
        fields = [
            'conviction_location', 'conviction_date', 'conviction_charge', 'conviction_penalty'
        ]


TrafficConvictionFormSet = formset_factory(TrafficConvictionForm, extra=1, max_num=3)


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = [
            'license_state', 'license_number', 'license_class', 'license_endorsements', 'license_expiration_date',
            'denied_license', 'suspended_license', 'license_details'
        ]


LicenseFormSet = formset_factory(LicenseForm, extra=1, max_num=4)
