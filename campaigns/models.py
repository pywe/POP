from django.db import models
from django.conf import settings
# Create your models here.


# First class model
class Country(models.Model):
    name = models.CharField(max_length=50,help_text="This is a country from anywhere in the world")

    def __str__(self):
        return self.name

statuses = (
    ('active','active'),
    ('inactive','inactive'),
    ('complete','complete')
)
# Second class Model
class Campaign(models.Model):
    name = models.CharField(max_length=200,unique=True)
    is_training = models.BooleanField(default=False,help_text="Is this a training campaign for analysts")
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=10,choices=statuses)


    def __str__(self):
        return "{} in {}".format(str(self.name),str(self.country))

# Second class Model
class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# Third class model
class District(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL,help_text="City in which Pharmacy can be found")

    def __str__(self):
        return self.name

# First class model
class Test(models.Model):
    name = models.CharField(max_length=50,help_text='Tests taken at pharmacies such as for hypertension, blood glucose')

    def __str__(self):
        return self.name


insurance_options = (
    ("Private Insurance","Private Insurance"),
    ("Public Insurance","Public Insurance"),
    ("No Insurance","No Insurance"),
    ("Undetermined","Undetermined")
)

standards = (
    ('A','A'),
    ('B+','B+'),
    ('B','B'),
    ('B-','B-'),
    ('C','C'),
)

district_standards = (
    ("Upper-Top quartile","Upper-Top quartile"),
    ("Average-2nd quartile","Average-2nd quartile"),
    ("Average-3rd quartile","Average-3rd quartile"),
    ("Lower-4th quartile","Lower-4th quartile")
)

district_profiles = (
    ('Residential','Residential'),
    ('Business','Business'),
    ('Other','Other')
)

staffs_followed = (
    ("Owner","Owner"),
    ("Pharmacist in chief","Pharmacist in chief"),
    ("Pharmacist assistant","Pharmacist assistant"),
    ("Technician","Technician"),
    ("Vendor","Vendor")
)

# Fourth class model
# migrate Test, City, and Country before this model
class Pharmacy(models.Model):
    name = models.CharField(max_length=200,unique=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=14,null=True,help_text="mobile phone number of the followed pharmacist (vendor)")
    # The area name will take care of the city and country of the pharmacy
    area_name = models.ForeignKey(District,null=True,on_delete=models.SET_NULL)
    detailed_address = models.TextField(null=True,help_text="Make this detailed to easily find pharmacy")
    pharmacist_first_name = models.CharField(max_length=150,null=True)
    pharmacist_last_name = models.CharField(max_length=150,null=True)
    average_patients_per_day = models.IntegerField(default=0,help_text="Average number of patients visiting the pharmacy per day")
    insurance_convention = models.CharField(max_length=100,choices=insurance_options,null=True)
    pharmacy_standard = models.CharField(max_length=5,choices=standards,null=True)
    district_social_standard = models.CharField(max_length=50,choices=district_standards,null=True)
    district_profile = models.CharField(max_length=20,choices=district_profiles,null=True)
    conselling = models.BooleanField(default=False)
    computerized = models.BooleanField(default=False)
    tests_available = models.ManyToManyField(Test)
    staff_mostly_followed = models.CharField(max_length=50,choices=staffs_followed,null=True)
    staff_mostly_present = models.CharField(max_length=50,choices=staffs_followed,null=True)
    dependent_on_hospital = models.BooleanField(default=False)
    comments = models.TextField(null=True,help_text="Any other things we should take notice of...")

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.SET_NULL)


# Fifth class model
class Basket(models.Model):
    pharmacy = models.ForeignKey(Pharmacy,null=True,on_delete=models.SET_NULL,help_text="Where this basket of drugs is being created")
    session = models.ForeignKey(Session,null=True,on_delete=models.SET_NULL,help_text="To what session is this tied?")


gender_options = (
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
)

# Sixth class model
# Basket must be migrated before this model:Will serve as inlines
class Patient(models.Model):
    basket = models.ForeignKey(Basket,null=True,on_delete=models.SET_NULL)
    insurance_scheme = models.CharField(max_length=100,choices=insurance_options,null=True)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=10,choices=gender_options,null=True)


drivers = (
    ("Patient","Patient"),
    ("Pharmacist","Pharmacist"),
    ("Prescriber","Prescriber")
)

switch_reasons = (
    ('Not available','Not available'),
    ('Price','Price'),
    ('Therapeutic Reason','Therapeutic Reason'),
    ('Other Reason','Other Reason')
)

# First class model
class drugForm(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

# First class model
class Company(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


# Second class model
class drugReference(models.Model):
    brand_name = models.CharField(max_length=200,null=True)
    dossage = models.CharField(max_length=10,null=True)
    inn = models.CharField(max_length=300,null=True,help_text="Active ingredient in the drug. eg. paracetamol")
    form = models.ForeignKey(drugForm,null=True,on_delete=models.SET_NULL,help_text="liquid,tablet")
    company = models.ForeignKey(Company,null=True,on_delete=models.SET_NULL,help_text="Manufacturing company")
    therapeutic_purpose = models.TextField(null=True)
    # therapeutic_class =


initials = (
    ("brand patient","brand patient"),
    ("brand prescription","brand prescription"),
    ("inn patient","inn patient"),
    ("inn prescription","inn prescription")
)


divisions = (
    ("unit","unit"),
    ("blister","blister"),
    ("box","box"),
    ("blister+unit","blister+unit"),
    ("box+unit","box+unit"),
    ("box+blister","box+blister")
)

# Sixth class model
# Basket must be migrated before this model:Will serve as inlines
class Drug(models.Model):
    basket = models.ForeignKey(Basket,null=True,on_delete=models.SET_NULL)
    initial_request = models.CharField(max_length=15,choices=initials,null=True,help_text="Who started the request?")
    # we will take the brand name from drugReference
    drug_sold = models.CharField(max_length=200,help_text="brand name of drug that has been sold?")
    sale_driver = models.CharField(max_length=15,choices=drivers,null=True,help_text="Who makes the final selection for the purchased product?")
    switched = models.BooleanField(default=False,help_text="Was there a switch?")
    leaked = models.BooleanField(default=False,help_text="Was there a leak?")
    # we will take the brand name from drugReference
    product_switched_or_leaked = models.CharField(max_length=200,help_text="What product was switched or leaked?")
    reason_for_switch_or_leak = models.CharField(max_length=50,choices=switch_reasons,null=True,help_text="Why was there a switch or a leak?")
    form_sold = models.ForeignKey(drugForm,null=True,on_delete=models.SET_NULL,help_text="What form of drug was sold? liquid,tablet")
    division = models.CharField(max_length=50,choices=divisions,null=True,help_text="Was the whole box sold? How was it divided?")

# First class model
class anatomicalClass(models.Model):
    code_name = models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name_plural = "anatomical classes"


    def __str__(self):
        return self.code_name




# Second class model
class therapeuticClass(models.Model):
    code_name = models.CharField(max_length=200,null=True)
    anatomical_class= models.ForeignKey(anatomicalClass,null=True,on_delete=models.SET_NULL)


    class Meta:
        verbose_name_plural = "therapeutic classes"

    def __str__(self):
        return self.code_name



# Thrid class model
class chemicalClass(models.Model):
    code_name = models.CharField(max_length=200,null=True)
    therapeutic_class = models.ForeignKey(therapeuticClass,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.code_name


class pharmacologicalClass(models.Model):
    code_name = models.CharField(max_length=200,null=True)
    chemical_class = models.ForeignKey(chemicalClass,null=True,on_delete=models.SET_NULL)


# Fourth class model
class Inn(models.Model):
    inn = models.CharField(max_length=100,null=True)
    inncode = models.CharField(max_length=200,null=True)
    # pharmacological_class = models.ForeignKey(pharmacologicalClass,null=True,on_delete=models.SET_NULL)
    chemical_class = models.ForeignKey(chemicalClass,null=True,on_delete=models.SET_NULL,help_text="Which chemical code does this substance match to?")


    def __str__(self):
        return self.inncode


# First class model Prescriber
class Prescriber(models.Model):
    name = models.CharField(max_length=50,choices = initials,null=True)


# First class model Division
class Division(models.Model):
    name = models.CharField(max_length=50,choices=divisions,null=True)

# First class model SwitchReason
class SwitchReason(models.Model):
    name = models.CharField(max_length=50,choices=switch_reasons,null=True)

# First class model SalesDriver
class SalesDriver(models.Model):
    name = models.CharField(max_length=50,choices=drivers,null=True)


# First class model StaffFollowed
class StaffFollowed(models.Model):
    name = models.CharField(max_length=50,choices=staffs_followed,null=True)


# First class model DistrictProfile
class DistrictProfile(models.Model):
    name = models.CharField(max_length=50,choices=district_profiles,null=True)

# First class model DistrictStandard
class DistrictStandard(models.Model):
    name = models.CharField(max_length=50,choices=district_standards,null=True)

# First class model PharmacyStandard
class PharmacyStandard(models.Model):
    name = models.CharField(max_length=50,choices=standards,null=True)


# First class model InsuranceType
class InsuranceType(models.Model):
    name = models.CharField(max_length=50,choices=insurance_options,null=True)

