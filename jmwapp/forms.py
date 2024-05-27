from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import JobApplication, EmploymentHistory, AccidentRecord, TrafficConviction, License


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        widgets = {
            'email_address': forms.TextInput(attrs={'type': 'email'}),
            'date_of_application': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'worked_here_from': forms.DateInput(attrs={'type': 'date'}),
            'worked_here_to': forms.DateInput(attrs={'type': 'date'}),
            'rate_of_pay': forms.NumberInput(attrs={'step': '1.00', 'class': 'monetary-field'}),
            'rate_of_pay_expected': forms.NumberInput(attrs={'step': '1.00', 'class': 'monetary-field'}),
            'phone_number': forms.TextInput(attrs={'id': 'id_phone_number'}),
            'social_security_number': forms.TextInput(attrs={'id': 'id_social_security_number'}),
        }


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
