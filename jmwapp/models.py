from django.db import models


class JobApplication(models.Model):
    # Top of application
    applicant_name = models.CharField(max_length=255, verbose_name="Applicant Name")
    date_of_application = models.DateField(verbose_name="Date of Application")
    email_address = models.CharField(max_length=50, verbose_name="Email Address")

    # Applicant to complete
    position_applied_for = models.CharField(max_length=255, verbose_name="Position(s) Applied For")
    social_security_number = models.CharField(max_length=11, verbose_name="Social Security No.")

    # Current address
    address = models.CharField(max_length=255, verbose_name="Current Address")
    city = models.CharField(max_length=255, verbose_name="City")
    state = models.CharField(max_length=2, verbose_name="State")
    zip = models.CharField(max_length=5, verbose_name="Zip Code")
    phone_number = models.CharField(max_length=14, verbose_name="Phone Number")
    time_living = models.DurationField(verbose_name="How Long? (yr./mo.)")

    legal_right_work = models.BooleanField(verbose_name="Do you have the legal right to work in the United States?")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    proof_of_age = models.BooleanField(verbose_name="Can you provide proof of age?")
    worked_here_before = models.BooleanField(verbose_name="Have you worked here before?")
    worked_here_from = models.DateField(blank=True, null=True, verbose_name="Worked here From")
    worked_here_to = models.DateField(blank=True, null=True, verbose_name="Worked here To")
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Rate of Pay", blank=True, null=True)
    previous_position = models.CharField(max_length=255, verbose_name="Position", blank=True, null=True)
    reason_for_leaving_here = models.TextField(blank=True, null=True, verbose_name="Reason for Leaving")
    currently_employed = models.BooleanField(verbose_name="Are you currently employed?")
    time_since_previously_employed = models.CharField(max_length=255, blank=True, null=True,
                                                      verbose_name="How long since last employment?")  # only if currently_employed is false
    who_referred = models.CharField(max_length=255, verbose_name="Who referred you?")
    rate_of_pay_expected = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Rate of Pay Expected")
    ever_been_bonded = models.BooleanField(verbose_name="Have you ever been bonded?")
    name_of_bonding_company = models.CharField(max_length=255, blank=True, null=True,
                                               verbose_name="Name of bonding company")  # only if ever_been_bonded is true
    unable_perform = models.BooleanField(
        verbose_name="Is there any reason you might be unable to perform the functions of the job for which you have applied [as described in the attached job description]?")
    reason_unable_perform = models.TextField(blank=True, null=True,
                                             verbose_name="If yes, explain if you wish.")  # only if unable_perform


class EmploymentHistory(models.Model):
    # Employment history 1
    employer_name = models.CharField(max_length=255, verbose_name="Employer Name")
    employer_address = models.CharField(max_length=255, verbose_name="Address")
    employer_city = models.CharField(max_length=255, verbose_name="City")
    employer_state = models.CharField(max_length=2, verbose_name="State")
    employer_zip = models.CharField(max_length=5, verbose_name="Zip")
    employer_contact = models.CharField(max_length=255, verbose_name="Contact Person")
    employer_phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    subject_to_fmcsr = models.BooleanField(verbose_name="Were you subject to the FMCSRs** while employed?")
    drug_alcohol_testing = models.BooleanField(
        verbose_name="Was your job designated as a safety-sensitive function in any DOT-regulated mode subject to the drug and alcohol testing requirements of 49 CFR part 40?")
    # Date
    from_employer = models.IntegerField(verbose_name="From")
    to_employer = models.IntegerField(verbose_name="To")
    position_held = models.CharField(max_length=255, verbose_name="Position Held")
    salary_wage = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Salary/Wage")
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name="Reason for Leaving")


class AccidentRecord(models.Model):
    # Accident record
    last_accident_date = models.DateField(verbose_name="Date")
    last_accident_nature = models.CharField(max_length=255,
                                            verbose_name="Nature of Accident (head-on, rear-end, upset, etc.)")
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


class License2(models.Model):
    denied_license = models.BooleanField(
        verbose_name="A. Have you ever been denied a license, permit or privilege to operate a motor vehicle?")
    suspended_license = models.BooleanField(
        verbose_name="B. Has any license, permit or privilege ever been suspended or revoked?")
    license_details = models.TextField(blank=True, null=True,
                                       verbose_name="If the answer to either A or B is yes, give details")  # if denied_license or suspended_license are true


class DrivingExperience(models.Model):
    choices = [
        ('van', 'Van'),
        ('tank', 'Tank'),
        ('flat', 'Flat'),
        ('dump', 'Dump'),
        ('refer', 'Refer')
    ]

    straight_truck = models.BooleanField(verbose_name="Straight Truck")
    straight_truck_type = models.CharField(max_length=20,
                                           choices=choices,
                                           verbose_name="Type")
    straight_truck_from = models.DateField(verbose_name="From")
    straight_truck_to = models.DateField(verbose_name="To")
    straight_truck_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    tractor_semi_trailer = models.BooleanField(verbose_name="Tractor and Semi-Trailer")
    tractor_semi_trailer_type = models.CharField(max_length=20,
                                                 choices=choices,
                                                 verbose_name="Type")
    tractor_semi_trailer_from = models.DateField(verbose_name="From")
    tractor_semi_trailer_to = models.DateField(verbose_name="To")
    tractor_semi_trailer_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    tractor_two_trailers = models.BooleanField(verbose_name="Tractor - Two Trailers")
    tractor_two_trailers_type = models.CharField(max_length=20,
                                                 choices=choices,
                                                 verbose_name="Type")
    tractor_two_trailers_from = models.DateField(verbose_name="From")
    tractor_two_trailers_to = models.DateField(verbose_name="To")
    tractor_two_trailers_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    tractor_three_trailers = models.BooleanField(verbose_name="Tractor - Three Trailers")
    tractor_three_trailers_type = models.CharField(max_length=20,
                                                   choices=choices,
                                                   verbose_name="Type")
    tractor_three_trailers_from = models.DateField(verbose_name="From")
    tractor_three_trailers_to = models.DateField(verbose_name="To")
    tractor_three_trailers_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    motorcoach_eight = models.BooleanField(verbose_name="Motor Coach (More than 8 passengers)")
    motorcoach_eight_from = models.DateField(verbose_name="From")
    motorcoach_eight_to = models.DateField(verbose_name="To")
    motorcoach_eight_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    motorcoach_fifteen = models.BooleanField(verbose_name="Motor Coach (More than 15 passengers)")
    motorcoach_fifteen_from = models.DateField(verbose_name="From")
    motorcoach_fifteen_to = models.DateField(verbose_name="To")
    motorcoach_fifteen_miles = models.IntegerField(verbose_name="Approximate # of Miles Total")

    states_operated_in = models.TextField(blank=True, null=True, verbose_name="List States Operated In For Last 5 Years")
    special_courses = models.TextField(blank=True, null=True, verbose_name="Show Special Courses Or Training That Will help You As a Driver")
    safe_driving_awards = models.TextField(blank=True, null=True, verbose_name="Which Safe Driving Awards Do You Hold And From Whom?")
