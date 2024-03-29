from django.contrib import admin
from .models import *


class BasketPatientInline(admin.TabularInline):
    model = Patient
    # readonly_fields = ['image_tag',]
    extra = 0

class BasketDrugInline(admin.TabularInline):
    model = Drug
    # readonly_fields = ['image_tag',]
    extra = 0

class BasketAdmin(admin.ModelAdmin):
    model = Basket
    ## Defines the list of fields displayed on admin page
    list_display = ['session',]
    inlines = [ BasketPatientInline,BasketDrugInline ]

class ChildInline(admin.TabularInline):
    model = Child
    # readonly_fields = ['image_tag',]
    extra = 0

class ParentAdmin(admin.ModelAdmin):
    model = Parent
    ## Defines the list of fields displayed on admin page
    list_display = ['first_name','last_name']
    inlines = [ ChildInline, ]

# Register your models here.

admin.site.register(anatomicalClass)
admin.site.register(Basket,BasketAdmin)
admin.site.register(drugForm)
admin.site.register(drugReference)
admin.site.register(Campaign)
admin.site.register(Company)
admin.site.register(chemicalClass)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Pharmacy)
admin.site.register(Inn)
admin.site.register(Test)
admin.site.register(therapeuticClass)
admin.site.register(Prescriber)
admin.site.register(Division)
admin.site.register(SwitchReason)
admin.site.register(SalesDriver)
admin.site.register(StaffFollowed)
admin.site.register(DistrictProfile)
admin.site.register(DistrictStandard)
admin.site.register(PharmacyStandard)
admin.site.register(InsuranceType)
admin.site.register(Session)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Child)

