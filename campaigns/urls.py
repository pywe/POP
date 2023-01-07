from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r"^api/v1/atc/create_atc/$",views.create_atc, name="create-atc"),
    url(r"^api/v1/atc/create_tc/$",views.create_therapeutic, name="create-tc"),

    # get apis
    url(r"^api/v1/pharmacy/get-pharmacies/$",views.get_pharmacies, name="get-pharmacies"),


    url(r"^api/v1/options/get-drug-references/$",views.get_drugreferences, name="get-drug-references"),
    url(r"^api/v1/options/get-inns/$",views.get_inns, name="get-inns"),
    url(r"^api/v1/options/get-prescribers/$",views.get_prescribers, name="get-prescribers"),
    url(r"^api/v1/options/get-divisions/$",views.get_divisions, name="get-divisions"),
    url(r"^api/v1/options/get-switch-reasons/$",views.get_switch_reasons, name="get-switch-reasons"),
    url(r"^api/v1/options/get-sales-drivers/$",views.get_sales_drivers, name="get-sales-drivers"),
    url(r"^api/v1/options/get-staff-followed/$",views.get_staffs_followed, name="get-staff-followed"),
    url(r"^api/v1/options/get-districts/$",views.get_districts, name="get-districts"),
    url(r"^api/v1/options/get-district-profiles/$",views.get_district_profiles, name="get-district-profiles"),
    url(r"^api/v1/options/get-district-standards/$",views.get_district_standards, name="get-district-standards"),
    url(r"^api/v1/options/get-pharmacy-standards/$",views.get_pharmacy_standards, name="get-pharmacy-standards"),
    url(r"^api/v1/options/get-insurance-types/$",views.get_insurance_types, name="get-insurance-types"),
    url(r"^api/v1/options/get-available-tests/$",views.get_tests_available, name="get-available-tests"),

    # creation apis
    url(r"^api/v1/campaigns/create-session/$",views.createSession, name="create-session"),
     url(r"^api/v1/campaigns/create-patient/$",views.createPatient, name="create-patient"),
    url(r"^api/v1/campaigns/create-pharmacy/$",views.createPharmacy, name="create-pharmacy"),
    url(r"^api/v1/campaigns/create-basket/$",views.createBasket, name="create-basket"),
    url(r"^api/v1/campaigns/create-drug/$",views.createDrug, name="create-drug"),
    url(r"^api/v1/campaigns/create-inn/$",views.createInn, name="create-inn"),
    url(r"^api/v1/campaigns/create-drug-reference/$",views.createDrugReference, name="create-drug-reference"),

    # church apis
    url(r"^api/v1/church/create-parent/$",views.createParent, name="create-parent"),
    url(r"^api/v1/church/create-children/$",views.createChildren, name="create-children"),
    url(r"^api/v1/church/get-parents/$",views.getParents, name="get-parents"),

    # views
    url(r"^campaigns/new-basket/$",views.new_basket,name="new-basket"),
    url(r"^campaigns/new-pharmacy/$",views.new_pharmacy,name="new-pharmacy"),
    url(r"^campaigns/new-session/$",views.new_session,name="new-session"),
    url(r"^campaigns/observation-session/$",views.observation_session,name="observation-session"),
    url(r"^campaigns/lockscreen/$",views.lockscreen,name="lockscreen"),
    url(r"^campaigns/edit-session/$",views.edit_session,name="edit-session"),
    url(r"^campaigns/edit-basket/$",views.edit_basket,name="edit-basket"),
    url(r"^campaigns/edit-pharmacy/$",views.edit_pharmacy,name="edit-pharmacy"),

    url(r"^church/$",views.church,name="church"),
    url(r"^gs-register/$",views.gs,name="gs-register"),
    url(r"^churchdata/$",views.churchdata,name="churchdata"),
    url(r"^sentiment/$",views.sentiment,name="sentiment"),
]