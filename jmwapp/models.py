from django.db import models


class JobApplication(models.Model):
    # Top of application
    applicant_name = models.CharField(max_length=255)
    date_of_application = models.DateField()

    # Applicant to complete
    position_applied_for = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    proof_of_age = models.BooleanField()
    worked_here_before = models.BooleanField()
    worked_here_location = models.CharField(max_length=255, blank=True, null=True)  # only if worked_here_before is true
    worked_here_from = models.DateField(blank=True, null=True)
    worked_here_to = models.DateField(blank=True, null=True)
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2)
    previous_position = models.CharField(max_length=255)
    reason_for_leaving = models.TextField(blank=True, null=True)
    currently_employed = models.BooleanField()
    time_since_previously_employed = models.CharField(max_length=255, blank=True, null=True)  # only if currently_employed is false
    who_referred = models.CharField(max_length=255)
    rate_of_pay_expected = models.DecimalField(max_digits=6, decimal_places=2)
    ever_been_bonded = models.BooleanField()
    name_of_bonding_company = models.CharField(max_length=255, blank=True, null=True)  # only if ever_been_bonded is true
    unable_perform = models.BooleanField()
    reason_unable_perform = models.TextField(blank=True, null=True)  # only if unable_perform

    # Current address
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

    # Employment history 1
    employer_name_1 = models.CharField(max_length=255)
    employer_address_1 = models.CharField(max_length=255)
    employer_city_1 = models.CharField(max_length=255)
    employer_state_1 = models.CharField(max_length=2)
    employer_zip_1 = models.CharField(max_length=5)
    employer_contact_1 = models.CharField(max_length=255)
    employer_phone_number_1 = models.CharField(max_length=255)
    subject_to_fmcsr_1 = models.BooleanField()
    drug_alcohol_testing_1 = models.BooleanField()
    # Date
    from_month_1 = models.IntegerField()
    from_year_1 = models.IntegerField()
    to_month_1 = models.IntegerField()
    to_year_1 = models.IntegerField()
    position_held_1 = models.CharField(max_length=255)
    salary_wage_1 = models.DecimalField(max_digits=6, decimal_places=2)
    reason_for_leaving_1 = models.CharField(max_length=255)

    # Employment history 2
    employer_name_2 = models.CharField(max_length=255)
    employer_address_2 = models.CharField(max_length=255)
    employer_city_2 = models.CharField(max_length=255)
    employer_state_2 = models.CharField(max_length=2)
    employer_zip_2 = models.CharField(max_length=5)
    employer_contact_2 = models.CharField(max_length=255)
    employer_phone_number_2 = models.CharField(max_length=255)
    subject_to_fmcsr_2 = models.BooleanField()
    drug_alcohol_testing_2 = models.BooleanField()
    # Date
    from_month_2 = models.IntegerField()
    from_year_2 = models.IntegerField()
    to_month_2 = models.IntegerField()
    to_year_2 = models.IntegerField()
    position_held_2 = models.CharField(max_length=255)
    salary_wage_2 = models.DecimalField(max_digits=6, decimal_places=2)
    reason_for_leaving_2 = models.CharField(max_length=255)

    # Employment history 3
    employer_name_3 = models.CharField(max_length=255)
    employer_address_3 = models.CharField(max_length=255)
    employer_city_3 = models.CharField(max_length=255)
    employer_state_3 = models.CharField(max_length=2)
    employer_zip_3 = models.CharField(max_length=5)
    employer_contact_3 = models.CharField(max_length=255)
    employer_phone_number_3 = models.CharField(max_length=255)
    subject_to_fmcsr_3 = models.BooleanField()
    drug_alcohol_testing_3 = models.BooleanField()
    # Date
    from_month_3 = models.IntegerField()
    from_year_3 = models.IntegerField()
    to_month_3 = models.IntegerField()
    to_year_3 = models.IntegerField()
    position_held_3 = models.CharField(max_length=255)
    salary_wage_3 = models.DecimalField(max_digits=6, decimal_places=2)
    reason_for_leaving_3 = models.CharField(max_length=255)

    # Employment history 4
    employer_name_4 = models.CharField(max_length=255)
    employer_address_4 = models.CharField(max_length=255)
    employer_city_4 = models.CharField(max_length=255)
    employer_state_4 = models.CharField(max_length=2)
    employer_zip_4 = models.CharField(max_length=5)
    employer_contact_4 = models.CharField(max_length=255)
    employer_phone_number_4 = models.CharField(max_length=255)
    subject_to_fmcsr_4 = models.BooleanField()
    drug_alcohol_testing_4 = models.BooleanField()
    # Date
    from_month_4 = models.IntegerField()
    from_year_4 = models.IntegerField()
    to_month_4 = models.IntegerField()
    to_year_4 = models.IntegerField()
    position_held_4 = models.CharField(max_length=255)
    salary_wage_4 = models.DecimalField(max_digits=6, decimal_places=2)
    reason_for_leaving_4 = models.CharField(max_length=255)

    # Employment history 5
    employer_name_5 = models.CharField(max_length=255)
    employer_address_5 = models.CharField(max_length=255)
    employer_city_5 = models.CharField(max_length=255)
    employer_state_5 = models.CharField(max_length=2)
    employer_zip_5 = models.CharField(max_length=5)
    employer_contact_5 = models.CharField(max_length=255)
    employer_phone_number_5 = models.CharField(max_length=255)
    subject_to_fmcsr_5 = models.BooleanField()
    drug_alcohol_testing_5 = models.BooleanField()
    # Date
    from_month_5 = models.IntegerField()
    from_year_5 = models.IntegerField()
    to_month_5 = models.IntegerField()
    to_year_5 = models.IntegerField()
    position_held_5 = models.CharField(max_length=255)
    salary_wage_5 = models.DecimalField(max_digits=6, decimal_places=2)
    reason_for_leaving_5 = models.CharField(max_length=255)

    # Accident record
    last_accident_date = models.DateField()
    last_accident_nature = models.CharField(max_length=255)
    last_accident_fatalities = models.CharField(max_length=255)
    last_accident_injuries = models.CharField(max_length=255)
    last_accident_spill = models.CharField(max_length=255)

    # Traffic Convictions
    conviction_location_1 = models.CharField(max_length=255)
    conviction_date_1 = models.DateField()
    conviction_charge_1 = models.CharField(max_length=255)
    conviction_penalty_1 = models.CharField(max_length=255)
    # Add more

    # Experience and Qualifications
    license_state_1 = models.CharField(max_length=2)
    license_number_1 = models.CharField(max_length=15)
    license_class_1 = models.CharField(max_length=10)
    license_endorsements_1 = models.CharField(max_length=255)
    license_expiration_date_1 = models.DateField()

    denied_license = models.BooleanField()
    suspended_license = models.BooleanField()
    license_details = models.TextField(blank=True, null=True)  # if denied_license or suspended_license are true
