from django.db import models


class JobApplication(models.Model):
    # Top of application
    applicant_name = models.CharField(max_length=255, verbose_name="Applicant Name")
    date_of_application = models.DateField(verbose_name="Date of Application")

    # Applicant to complete
    position_applied_for = models.CharField(max_length=255, verbose_name="Position(s) Applied For")
    social_security_number = models.CharField(max_length=11, verbose_name="Social Security No.")

    # Current address
    address = models.CharField(max_length=255, verbose_name="Current Address")
    city = models.CharField(max_length=255, verbose_name="City")
    state = models.CharField(max_length=2, verbose_name="State")
    zip = models.IntegerField(verbose_name="Zip Code")
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number")
    time_living = models.DurationField(verbose_name="How Long? (yr./mo.)")

    legal_right_work = models.BooleanField(verbose_name="Do you have the legal right to work in the United States?")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    proof_of_age = models.BooleanField(verbose_name="Can you provide proof of age?")
    worked_here_before = models.BooleanField(verbose_name="Have you worked here before?")
    worked_here_from = models.DateField(blank=True, null=True, verbose_name="Worked here From")
    worked_here_to = models.DateField(blank=True, null=True, verbose_name="Worked here To")
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Rate of Pay")
    previous_position = models.CharField(max_length=255, verbose_name="Position")
    reason_for_leaving_here = models.TextField(blank=True, null=True, verbose_name="Reason for Leaving")
    currently_employed = models.BooleanField(verbose_name="Are you currently employed?")
    time_since_previously_employed = models.CharField(max_length=255, blank=True, null=True, verbose_name="How long since last employment?")  # only if currently_employed is false
    who_referred = models.CharField(max_length=255, verbose_name="Who referred you?")
    rate_of_pay_expected = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Rate of Pay Expected")
    ever_been_bonded = models.BooleanField(verbose_name="Have you ever been bonded?")
    name_of_bonding_company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name of bonding company")  # only if ever_been_bonded is true
    unable_perform = models.BooleanField(verbose_name="Is there any reason you might be unable to perform the functions of the job for which you have applied [as described in the attached job description]?")
    reason_unable_perform = models.TextField(blank=True, null=True, verbose_name="If yes, explain if you wish.")  # only if unable_perform


class EmploymentHistory(models.Model):
    # Employment history 1
    employer_name = models.CharField(max_length=255, verbose_name="Employer Name")
    employer_address = models.CharField(max_length=255, verbose_name="Address")
    employer_city = models.CharField(max_length=255, verbose_name="City")
    employer_state = models.CharField(max_length=2, verbose_name="State")
    employer_zip = models.CharField(max_length=5, verbose_name="Zip")
    employer_contact = models.CharField(max_length=255, verbose_name="Contact Person")
    employer_phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    subject_to_fmcsr = models.BooleanField(verbose_name="Were you subject to the FMCSRs while employed?")
    drug_alcohol_testing = models.BooleanField(verbose_name="Was your job designated as a safety-sensitive function in any DOT-regulated mode subject to the drug and alcohol testing requirements of 49 CFR part 40?")
    # Date
    from_month = models.IntegerField(verbose_name="From Mo.")
    from_year = models.IntegerField(verbose_name="From Yr.")
    to_month = models.IntegerField(verbose_name="To Mo.")
    to_year = models.IntegerField(verbose_name="To Yr.")
    position_held = models.CharField(max_length=255, verbose_name="Position Held")
    salary_wage = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Salary/Wage")
    reason_for_leaving = models.CharField(max_length=255, verbose_name="Reason for Leaving")


class AccidentRecord(models.Model):
    # Accident record
    last_accident_date = models.DateField(verbose_name="Date")
    last_accident_nature = models.CharField(max_length=255, verbose_name="Nature of Accident (head-on, rear-end, upset, etc.)")
    last_accident_fatalities = models.BooleanField(verbose_name="Fatalities?")
    last_accident_injuries = models.BooleanField(verbose_name="Injuries?")
    last_accident_spill = models.BooleanField(verbose_name="Hazardous material spill?")


class TrafficConviction(models.Model):
    # Traffic Convictions
    conviction_location = models.CharField(max_length=255, verbose_name="Location")
    conviction_date = models.DateField(verbose_name="Date")
    conviction_charge = models.CharField(max_length=255, verbose_name="Charge")
    conviction_penalty = models.CharField(max_length=255, verbose_name="Penalty")


class License(models.Model):
    # Experience and Qualifications
    license_state = models.CharField(max_length=2, verbose_name="State")
    license_number = models.CharField(max_length=15, verbose_name="License No.")
    license_class = models.CharField(max_length=10, verbose_name="Class")
    license_endorsements = models.CharField(max_length=255, verbose_name="Endorsement(s)")
    license_expiration_date = models.DateField(verbose_name="Expiration Date")

    denied_license = models.BooleanField(verbose_name="A. Have you ever been denied a license, permit or privilege to operate a motor vehicle?")
    suspended_license = models.BooleanField(verbose_name="B. Has any license, permit or privilege ever been suspended or revoked?")
    license_details = models.TextField(blank=True, null=True, verbose_name="If the answer to either A or B is yes, give details")  # if denied_license or suspended_license are true
