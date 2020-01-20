from django.shortcuts import render,redirect,HttpResponse
import json
# from tastypie.models import ApiKey
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.



# Create anatomical classes using api
@csrf_exempt
def create_atc(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    name = json_data['atccode']
    atc = anatomicalClass()
    atc.code_name = name
    atc.save()
    data = {'success':True,'message':'atc created'}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


# Create anatomical classes using api
@csrf_exempt
def create_therapeutic(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    name = json_data['codename']
    atc = json_data['atc']
    atc = anatomicalClass.objects.get(code_name=atc)
    tc = therapeuticClass()
    tc.code_name = name
    tc.anatomical_class = atc
    tc.save()
    data = {'success':True,'message':'tc created'}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_pharmacies(request):
    pharmacies = Pharmacy.objects.all()
    objects = []
    for i in pharmacies:
        obj = {}
        obj['name']=i.name
        obj['id']=i.id
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_drugreferences(request):
    references = drugReference.objects.all()
    objects = []
    for i in references:
        obj = {}
        obj['name']=i.brand_name
        obj['inn']=i.inn
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_inns(request):
    inns = Inn.objects.all()
    objects = []
    for i in inns:
        obj = {}
        obj['inn']=i.inn
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

@csrf_exempt
def get_prescribers(request):
    objs = Prescriber.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_divisions(request):
    objs = Division.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_switch_reasons(request):
    objs = SwitchReason.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_sales_drivers(request):
    objs = SalesDriver.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_staffs_followed(request):
    objs = StaffFollowed.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_district_profiles(request):
    objs = DistrictProfile.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

@csrf_exempt
def get_district_standards(request):
    objs = DistrictStandard.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_pharmacy_standards(request):
    objs = PharmacyStandard.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_insurance_types(request):
    objs = InsuranceType.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


