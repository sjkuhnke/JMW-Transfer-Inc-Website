from django.db import models


states = [
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
]

boolean = [
    ('yes', 'Yes'),
    ('no', 'No')
]


class JobApplication(models.Model):
    # Top of application
    first_name = models.CharField(max_length=255, verbose_name="Applicant First Name")
    last_name = models.CharField(max_length=255, verbose_name="Applicant Last Name")
    date_of_application = models.DateField(verbose_name="Date of Application")
    email_address = models.CharField(max_length=50, verbose_name="Email Address")

    # Applicant to complete
    position_applied_for = models.CharField(max_length=255, verbose_name="Position(s) Applied For")
    middle_initial = models.CharField(max_length=1, verbose_name="Middle Initial", blank=True, null=True)
    phone_number = models.CharField(max_length=14, verbose_name="Phone Number")
    social_security_number = models.CharField(max_length=11, verbose_name="Social Security No.")

    legal_right_work = models.CharField(max_length=100,
                                        choices=boolean,
                                        verbose_name="Do you have the legal right to work in the United States?")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    proof_of_age = models.CharField(max_length=100,
                                    choices=boolean,
                                    verbose_name="Can you provide proof of age?")
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
    unable_perform = models.CharField(max_length=100,
                                      choices=boolean,
                                      verbose_name="Is there any reason you might be unable to perform the functions of the job for which you have applied [as described in the attached job description]?")
    reason_unable_perform = models.TextField(blank=True, null=True,
                                             verbose_name="If yes, explain if you wish.")  # only if unable_perform


class Address(models.Model):
    duration = [
        ('mos', 'Months'),
        ('yrs', 'Years'),
    ]
    address = models.CharField(max_length=255, verbose_name="Address")
    city = models.CharField(max_length=255, verbose_name="City")
    state = models.CharField(max_length=100, choices=states, verbose_name="State")
    zip = models.CharField(max_length=5, verbose_name="Zip Code")
    time_living = models.IntegerField(verbose_name="How Long? (yr./mo.)")
    units = models.CharField(max_length=255, verbose_name="Select", choices=duration)


class EmploymentHistory(models.Model):
    employer_name = models.CharField(max_length=255, verbose_name="Employer Name")
    employer_address = models.CharField(max_length=255, verbose_name="Address")
    employer_city = models.CharField(max_length=255, verbose_name="City")
    employer_state = models.CharField(max_length=100, choices=states, verbose_name="State")
    employer_zip = models.CharField(max_length=5, verbose_name="Zip")
    employer_contact = models.CharField(max_length=255, verbose_name="Contact Person")
    employer_phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    subject_to_fmcsr = models.CharField(max_length=100,
                                        choices=boolean,
                                        verbose_name="Were you subject to the FMCSRs** while employed?")
    drug_alcohol_testing = models.CharField(max_length=100,
                                            choices=boolean,
                                            verbose_name="Was your job designated as a safety-sensitive function in any DOT-regulated mode subject to the drug and alcohol testing requirements of 49 CFR part 40?")
    # Date
    from_employer = models.IntegerField(verbose_name="From")
    to_employer = models.IntegerField(verbose_name="To")
    position_held = models.CharField(max_length=255, verbose_name="Position Held")
    salary_wage = models.CharField(max_length=100, verbose_name="Salary/Wage")
    reason_for_leaving = models.TextField(blank=True, null=True, verbose_name="Reason for Leaving")


class AccidentRecord(models.Model):
    # Accident record
    accident_date = models.DateField(verbose_name="Date")
    accident_nature = models.CharField(max_length=255,
                                            verbose_name="Nature of Accident (head-on, rear-end, upset, etc.)")
    accident_fatalities = models.CharField(max_length=100,
                                                choices=boolean,
                                                verbose_name="Any Fatalities?")
    accident_injuries = models.CharField(max_length=100,
                                              choices=boolean,
                                              verbose_name="Any Injuries?")
    accident_spill = models.CharField(max_length=100,
                                           choices=boolean,
                                           verbose_name="Any hazardous material spill?")


class TrafficConviction(models.Model):
    # Traffic Convictions
    conviction_location = models.CharField(max_length=255, verbose_name="Location")
    conviction_date = models.DateField(verbose_name="Date")
    conviction_charge = models.CharField(max_length=255, verbose_name="Charge")
    conviction_penalty = models.CharField(max_length=255, verbose_name="Penalty")


class License(models.Model):
    # Experience and Qualifications
    license_state = models.CharField(max_length=100, choices=states, verbose_name="State")
    license_number = models.CharField(max_length=20, verbose_name="License No. (include dashes)")
    license_class = models.CharField(max_length=10, verbose_name="Class")
    license_endorsements = models.CharField(max_length=255, verbose_name="Endorsement(s)")
    license_expiration_date = models.DateField(verbose_name="Expiration Date")


class License2(models.Model):
    denied_license = models.CharField(max_length=100,
                                      choices=boolean,
                                      verbose_name="A. Have you ever been denied a license, permit or privilege to operate a motor vehicle?")
    suspended_license = models.BooleanField(max_length=100,
                                            choices=boolean,
                                            verbose_name="B. Has any license, permit or privilege ever been suspended or revoked?")
    license_details = models.TextField(blank=True, null=True,
                                       verbose_name="If the answer to either A or B is yes, give details")  # if denied_license or suspended_license are true


class ApplicableCheckboxes(models.Model):
    employer_checkbox = models.BooleanField(verbose_name="No employment history")
    accident_checkbox = models.BooleanField(verbose_name="No accident records")
    conviction_checkbox = models.BooleanField(verbose_name="No traffic convictions")
    license_checkbox = models.BooleanField(verbose_name="No license information")


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

    other_name = models.CharField(max_length=40, verbose_name="Class", blank=True, null=True)
    other_type = models.CharField(max_length=20, verbose_name="Type", blank=True, null=True)
    other_from = models.DateField(verbose_name="From", blank=True, null=True)
    other_to = models.DateField(verbose_name="To", blank=True, null=True)
    other_miles = models.IntegerField(verbose_name="Approximate # of Miles Total", blank=True, null=True)

    states_operated_in = models.TextField(verbose_name="List States Operated In For Last 5 Years (NONE if none)")
    special_courses = models.CharField(max_length=50, verbose_name="Show Special Courses Or Training That Will help You As a Driver (NONE if none)")
    safe_driving_awards = models.CharField(max_length=50, verbose_name="Which Safe Driving Awards Do You Hold And From Whom? (NONE if none)")


class ExperienceQualifications(models.Model):
    school = [
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        (4, 'Grade 4'),
        (5, 'Grade 5'),
        (6, 'Grade 6'),
        (7, 'Grade 7'),
        (8, 'Grade 8'),
        (9, '1st Year High School'),
        (10, '2nd Year High School'),
        (11, '3rd Year High School'),
        (12, '4th Year High School'),
        (13, '1st Year College'),
        (14, '2nd Year College'),
        (15, '3rd Year College'),
        (16, '4th Year College'),
    ]

    trucking_experience = models.TextField(verbose_name="Show any trucking, transportation, or other experience that may help in your work for this company")
    courses_other = models.TextField(verbose_name="List courses and training other than shown elsewhere in this application")
    special_equipment = models.TextField(verbose_name="List special equipment or technical materials you can work with (other than those already shown)")
    highest_grade_completed = models.CharField(max_length=20,
                                                  choices=school,
                                                  verbose_name="Select highest grade completed")
    last_school_attended_name = models.CharField(max_length=255, verbose_name="Name of School")
    last_school_attended_city = models.CharField(max_length=255, verbose_name="City")
    last_school_attended_state = models.CharField(max_length=100, choices=states, verbose_name="State")


class Signature(models.Model):
    signature = models.CharField(max_length=255, verbose_name="Electronic Signature")
    date = models.DateField(verbose_name="Date")
