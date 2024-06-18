from django import forms
from django.forms import formset_factory
from .models import JobApplication, EmploymentHistory, AccidentRecord, TrafficConviction, License, License2, \
    DrivingExperience, ExperienceQualifications, Signature, ApplicableCheckboxes, Address


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
            'rate_of_pay': forms.TextInput(attrs={'step': '1.00', 'class': 'monetary-field'}),
            'rate_of_pay_expected': forms.TextInput(attrs={'step': '1.00', 'class': 'monetary-field'}),
            'phone_number': forms.TextInput(attrs={'id': 'id_phone_number'}),
            'social_security_number': forms.TextInput(attrs={'id': 'id_social_security_number'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


AddressFormset = formset_factory(AddressForm, extra=1, max_num=4)


class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'employer_name', 'employer_address', 'employer_city', 'employer_state',
            'employer_zip', 'employer_contact', 'employer_phone_number', 'subject_to_fmcsr',
            'drug_alcohol_testing', 'from_employer', 'to_employer',
            'position_held', 'salary_wage', 'reason_for_leaving'
        ]
        widgets = {
            'from_employer': forms.DateInput(attrs={'type': 'date'}),
            'to_employer': forms.DateInput(attrs={'type': 'date'}),
            'employer_phone_number': forms.TextInput(attrs={'id': 'id_employer_phone_number'}),
            'salary_wage': forms.TextInput(attrs={'step': '1.00', 'class': 'monetary-field'}),
        }


EmploymentHistoryFormSet = formset_factory(EmploymentHistoryForm, extra=1, max_num=5)


class AccidentRecordForm(forms.ModelForm):
    class Meta:
        model = AccidentRecord
        fields = [
            'accident_date', 'accident_nature', 'accident_fatalities', 'accident_injuries',
            'accident_spill'
        ]
        widgets = {
            'accident_date': forms.DateInput(attrs={'type': 'date'}),
        }


AccidentRecordFormSet = formset_factory(AccidentRecordForm, extra=1, max_num=3)


class TrafficConvictionForm(forms.ModelForm):
    class Meta:
        model = TrafficConviction
        fields = [
            'conviction_location', 'conviction_date', 'conviction_charge', 'conviction_penalty'
        ]
        widgets = {
            'conviction_date': forms.DateInput(attrs={'type': 'date'}),
        }


TrafficConvictionFormSet = formset_factory(TrafficConvictionForm, extra=1, max_num=3)


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = [
            'license_state', 'license_number', 'license_class', 'license_endorsements', 'license_expiration_date',
        ]
        widgets = {
            'license_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


LicenseFormSet = formset_factory(LicenseForm, extra=1, max_num=4)


class ApplicableCheckboxesForm(forms.ModelForm):
    class Meta:
        model = ApplicableCheckboxes
        fields = [
            'employer_checkbox', 'accident_checkbox', 'conviction_checkbox', 'license_checkbox'
        ]


class License2Form(forms.ModelForm):
    class Meta:
        model = License2
        fields = [
            'denied_license', 'suspended_license', 'license_details'
        ]


class DrivingExperienceForm(forms.ModelForm):
    class Meta:
        model = DrivingExperience
        fields = [
            'straight_truck', 'straight_truck_type', 'straight_truck_to', 'straight_truck_from', 'straight_truck_miles',
            'tractor_semi_trailer', 'tractor_semi_trailer_type', 'tractor_semi_trailer_from', 'tractor_semi_trailer_to',
            'tractor_semi_trailer_miles',
            'tractor_two_trailers', 'tractor_two_trailers_type', 'tractor_two_trailers_from', 'tractor_two_trailers_to',
            'tractor_two_trailers_miles',
            'tractor_three_trailers', 'tractor_three_trailers_type', 'tractor_three_trailers_from',
            'tractor_three_trailers_to', 'tractor_three_trailers_miles',
            'motorcoach_eight', 'motorcoach_eight_from', 'motorcoach_eight_to', 'motorcoach_eight_miles',
            'motorcoach_fifteen', 'motorcoach_fifteen_from', 'motorcoach_fifteen_to', 'motorcoach_fifteen_miles',
            'states_operated_in', 'special_courses', 'safe_driving_awards'
        ]
        widgets = {
            'straight_truck_from': forms.DateInput(attrs={'type': 'date'}),
            'straight_truck_to': forms.DateInput(attrs={'type': 'date'}),
            'straight_truck_miles': forms.NumberInput(attrs={'step': '50'}),
            'tractor_semi_trailer_from': forms.DateInput(attrs={'type': 'date'}),
            'tractor_semi_trailer_to': forms.DateInput(attrs={'type': 'date'}),
            'tractor_semi_trailer_miles': forms.NumberInput(attrs={'step': '50'}),
            'tractor_two_trailers_from': forms.DateInput(attrs={'type': 'date'}),
            'tractor_two_trailers_to': forms.DateInput(attrs={'type': 'date'}),
            'tractor_two_trailers_miles': forms.NumberInput(attrs={'step': '50'}),
            'tractor_three_trailers_from': forms.DateInput(attrs={'type': 'date'}),
            'tractor_three_trailers_to': forms.DateInput(attrs={'type': 'date'}),
            'tractor_three_trailers_miles': forms.NumberInput(attrs={'step': '50'}),
            'motorcoach_eight_from': forms.DateInput(attrs={'type': 'date'}),
            'motorcoach_eight_to': forms.DateInput(attrs={'type': 'date'}),
            'motorcoach_eight_miles': forms.NumberInput(attrs={'step': '50'}),
            'motorcoach_fifteen_from': forms.DateInput(attrs={'type': 'date'}),
            'motorcoach_fifteen_to': forms.DateInput(attrs={'type': 'date'}),
            'motorcoach_fifteen_miles': forms.NumberInput(attrs={'step': '50'}),
        }


class ExperienceQualificationsForm(forms.ModelForm):
    class Meta:
        model = ExperienceQualifications
        fields = [
            'trucking_experience', 'courses_other', 'special_equipment', 'highest_grade_completed',
            'last_school_attended_name', 'last_school_attended_city', 'last_school_attended_state'
        ]


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = [
            'signature', 'date'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
