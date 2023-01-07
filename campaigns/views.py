from django.shortcuts import render,redirect,HttpResponse
import json
# from tastypie.models import ApiKey
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.fields.files import ImageFieldFile
from django.apps import apps
import json
import csv
from accounts.models import CustomUser


campaign_models = apps.get_app_config('campaigns').get_models()
campaign_objects = {}
for model in campaign_models:
    campaign_objects[model.__name__]=model
    campaign_objects['CustomUser']=CustomUser
    # print(type(model.__name__))




def json2csv(name):
    with open('/home/Learn/observe/media/{}.json'.format(name)) as json_file:
        h = json.load(json_file)

    # accessing questions directly from ordered dicts
    mydata = h['objects']
    childdata = h['objects']
    # parents = {}
    # for each in mydata:
    #     parents[str(each['parent']['id'])] = each['parent']
    # print(parents)

    # now we will open a file for writing

    parent_file = open('/home/Learn/observe/media/{}.csv'.format("children"), 'w+')

    # create the csv writer object
    parent_writer = csv.writer(parent_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for quest in mydata:
        # print(quest)
        if count == 0:
            # Writing headers of CSV file
            # quest['parent']['children']=''
            header = quest.keys()
            parent_writer.writerow(header)
            count += 1
        # Writing data of CSV file
        # quest['parent']['children'] = len(quest['children'])
        h = parent_writer.writerow(quest.values())
        # print(h)
    parent_file.close()
    # data_file = open('/home/Learn/observe/media/children.csv', 'w+')
    # # create the csv writer object
    # csv_writer = csv.writer(data_file)
    # parent_file.close()


    # count = 0
    # for quest in childdata:
    #     for i in quest['children']:

    #         if count == 0:
    #             # Writing headers of CSV file
    #             header = i.keys()
    #             csv_writer.writerow(header)
    #             count += 1

    #         # Writing data of CSV file
    #         # print(list(quest[list(i.keys())[1]].values())[1:])
    #         csv_writer.writerow(i.values())
    # data_file.close()

    # f = open('/home/Learn/observe/campaigns/templates/{}.csv'.format(name), 'r+')
    # reader = csv.reader(f)
    # mylist = list(reader)
    # f.close()
    # for i,row in enumerate(mylist):
    #     # print(row)
    #     if(i > 0):
    #         row[1] = parents[row[1]]
    # # mylist[1][1] = 'X'
    # my_new_list = open('/home/Learn/observe/campaigns/templates/{}.csv'.format('children'), 'w', newline = '')
    # csv_writer = csv.writer(my_new_list)
    # csv_writer.writerows(mylist)

class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, ImageFieldFile):
            try:
                mypath = o.path
            except:
                return ''
            else:
                return mypath
        # this will either recusively return all atrributes of the object or return just the id
        elif isinstance(o, Model):
            # return model_to_dict(o)
            return o.id

        return super().default(o)

class ExtendedEncoderAllFields(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, ImageFieldFile):
            try:
                mypath = o.path
            except:
                return ''
            else:
                return mypath
        # this will either recusively return all atrributes of the object or return just the id
        elif isinstance(o, Model):
            return model_to_dict(o)
            # return o.id

        return super().default(o)

def getRelatedName(model,field):
    "Get the model to which a field is related"
    return model._meta.get_field(field).related_model.__name__


def raltionship(model,field):
    "What relationship does this field hold"
    if model._meta.get_field(field).many_to_one:
        return "many_to_one"
    elif model._meta.get_field(field).many_to_many:
        return "many_to_many"
    elif model._meta.get_field(field).one_to_one:
        return "one_to_one"
    elif model._meta.get_field(field).one_to_many:
        return "one_to_many"
    else:
        return "no_relation"

class Activity:
    # class constructor, initializer
    def __init__(self,modelName):
        self.modelName = modelName
        self.objects = campaign_objects

    # class method
    def create(self,**kwargs):
        # model = apps.get_model('Accounts', self.modelName)
        try:
            # creating instance as django model object based on passed modelName string
            instance = self.objects[self.modelName]()
            instance.save()
            # This error may usually be KeyError
        except Exception as e:
            return {'success':False,'message':str(e)}
        else:
            # Now, let's use passed keyword arguments to set field values for our instance
            for key,val in kwargs.items():
                try:
                    main = self.modelName
                    if raltionship(self.objects[main],key) == "many_to_one":
                        # TODO: create new objects recersively from relations
                        try:
                            rel_name = getRelatedName(self.objects[main],key)
                            child_model = self.objects[rel_name]
                            children = child_model.objects.get(id=int(val))
                        except Exception as e:
                            pass
                            # return {'success':False,'message':str(e)}
                        else:
                            try:
                                instance.__setattr__(key,children)
                            except Exception as e:
                                return {'success':False,'message':str(e)}
                            else:
                                try:
                                    instance.save()
                                except Exception as e:
                                    return {'success':False,'message':str(e)}
                    # is the field a many to many key
                    elif raltionship(self.objects[self.modelName],key) == "many_to_many":
                        try:
                            rel_name = getRelatedName(self.objects[main],key)
                            child_model = self.objects[rel_name]
                            children = [child_model.objects.get(id=int(i)) for i in val]
                        except Exception as e:
                            return {'success':False,'message':str(e)}
                        else:
                            try:
                                # field = self.objects[self.modelName]._meta.get_field(key)
                                # field.set(children)
                                # instance.__setattr__(key,children)
                                if key == "tests_available":
                                    instance.tests_available.add(*children)
                            except Exception as e:
                                return {'success':False,'message':str(e)}
                            else:
                                try:
                                    instance.save()
                                except Exception as e:
                                    return {'success':False,'message':str(e)}
                    else:
                        try:
                            instance.__setattr__(key,val)
                        except Exception as e:
                            return {'success':False,'message':str(e)}
                except:
                    pass
                    # # is the field a foreign key
                    # main = self.modelName
                    # if raltionship(self.objects[main],key) == "many_to_one":
                    #     # TODO: create new objects recersively from relations
                    #     try:
                    #         rel_name = getRelatedName(self.objects[main],key)
                    #         child_model = self.objects[rel_name]
                    #         children = child_model.objects.get(id=int(val))
                    #     except Exception as e:
                    #         return {'success':False,'message':str(e)}
                    #     try:
                    #         instance.__setattr__(key,children)
                    #     except Exception as e:
                    #         return {'success':False,'message':str(e)}
                    #     instance.save()
                    # # is the field a many to many key
                    # if raltionship(self.objects[self.modelName],key) == "many_to_many":
                    #     try:
                    #         rel_name = getRelatedName(self.objects[self.modelName],key)
                    #         child_model = self.objects[rel_name]
                    #         children = [child_model.objects.get(id=int(i)) for i in val]
                    #     except Exception as e:
                    #         return {'success':False,'message':str(e)}
                    #     instance.save()
                    # try:
                    #     instance.__setattr__(key,children)
                    # except Exception as e:
                    #     return {'success':False,'message':str(e)}
                    # instance.save()
                else:
                    instance.save()
                 # is the field a foreign key

            # try:
            #     instance.__setattr__(key,children)
            # except Exception as e:
            #     return {'success':False,'message':str(e)}
            # instance.save()
        # adding parents to the object (may be more than one parent
        # if parents:
        #     for parent in parents:
        #         try:
        #             parent = parent['name']
        #             instance.__setattr__(parent,parent['value'])
        #             instance.save()
        #         except:
        #             pass
        return {'success':True,'message':'successful','data':instance}

    # reads from database the particular model instance given
    # TODO: add specific field to be returned as **kwargs
    def read(self,key_id,primary_key,*fields):
        # setting the model based on passed model string
        # and getting all fields of the model
        allfields = self.objects[self.modelName]._meta.get_fields()
        # setting instance as passed instance
        instance = self.objects[self.modelName].__getattr__.get(key_id,primary_key)
        names = []
        vals = []
        # here we get all the available fields on a particular instance
        # this means if the field is not yet created but exists on the model, it will not be taken
        objects = {}
        # This will use user defined field when return the object requested
        if fields:
            for field in fields:
                try:
                    val = (getattr(instance, field))
                except:
                    pass
                else:
                    names.append(field)
                    try:
                        obj = list(val.values())
                    except:
                        vals.append(val)
                    else:
                        vals.append(obj)
            for i,e in enumerate(names):
                objects[e]=vals[i]

        else:
            # this will return all available fields on the instance
            for field in allfields:
                try:
                    val = (getattr(instance, field.name))
                except:
                    pass
                else:
                    names.append(field.name)
                    try:
                        obj = list(val.values())
                    except:
                        vals.append(val)
                    else:
                        vals.append(obj)
            for i,e in enumerate(names):
                objects[e]=vals[i]
            # our return dictionary contains fields with their values even ManyToMany or related field
            # Already serialized
        dump = json.dumps(objects,cls=ExtendedEncoder)
        return {'success':True,'data':dump}

    # class method to update object
    def update(self,key_id,primary_key,**kwargs):
        try:
            instance = self.objects[self.modelName].__getattr__.get(key_id,primary_key)
        except Exception as e:
            return False
        else:
            for key,val in kwargs.items():
                try:
                    instance.__setattr__(key,val)
                except:
                    pass
            instance.save()
        return {'success':True}


    # class method to delete instance of the model
    def delete(self,key_id,primary_key):
        try:
            instance = self.objects[self.modelName].__getattr__.get(key_id,primary_key)
        except Exception as e:
            return False
        else:
            instance.delete()
            return {'success':True}

# Create your views here.
def campaign_list(request):
    template_name = "campaigns/campaign_list.html"
    args = {}
    return render(request,template_name,args)

def church(request):
    template_name = "campaigns/church-file.html"
    args = {}
    return render(request,template_name,args)

def gs(request):
    template_name = "campaigns/gs.html"
    args = {}
    return render(request,template_name,args)

def sentiment(request):
    template_name = "campaigns/analyzer.html"
    args = {}
    return render(request,template_name,args)

def churchdata(request):
    template_name = "campaigns/downloadpage.html"
    args = {}
    objects = []
    objs = Child.objects.all()

    for i in objs:
        obj = model_to_dict(i)
        obj["child first name"] = obj["first_name"]
        obj["child last name"] = obj["last_name"]
        del obj["first_name"]
        del obj["last_name"]
        parent = model_to_dict(Parent.objects.get(id=int(i.parent.id)))
        parent["parent first name"] = parent["first_name"]
        parent["parent last name"] = parent["last_name"]
        del parent["first_name"]
        del parent["last_name"]
        # obj['parent']=i
        # obj['children'] = [i for i in i.children.all()]
        # i.parent =
        merged = {**parent,**obj}
        del merged['id']
        del merged['parent']
        objects.append(merged)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data,sort_keys=True,indent=4,cls=ExtendedEncoderAllFields)
    newfile = open("/home/Learn/observe/media/{}.json".format("kpehe"),'w+')
    newfile.write(dump)
    newfile.close()
    json2csv("kpehe")
    args['parents'] = 'parents.csv'
    args['children'] = 'children.csv'
    return render(request,template_name,args)


def new_basket(request):
    template_name = "campaigns/new-basket.html"
    args = {}
    return render(request,template_name,args)


def new_session(request):
    template_name = "campaigns/new-session.html"
    args = {}
    return render(request,template_name,args)

def edit_session(request):
    template_name = "campaigns/edit-session.html"
    args = {}
    return render(request,template_name,args)

def edit_basket(request):
    template_name = "campaigns/edit-basket.html"
    args = {}
    return render(request,template_name,args)

def edit_pharmacy(request):
    template_name = "campaigns/edit-pharmacy.html"
    args = {}
    return render(request,template_name,args)


def new_pharmacy(request):
    template_name = "campaigns/new-pharmacy.html"
    args = {}
    return render(request,template_name,args)


def observation_session(request):
    template_name = "campaigns/observation-session.html"
    args = {}
    return render(request,template_name,args)

def lockscreen(request):
    template_name = "campaigns/lockscreen.html"
    args = {}
    return render(request,template_name,args)


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

@csrf_exempt
def get_districts(request):
    objs = District.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['id']=i.id
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def get_tests_available(request):
    objs = Test.objects.all()
    objects = []
    for i in objs:
        obj = {}
        obj['id']=i.id
        obj['name']=i.name
        objects.append(obj)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')



@csrf_exempt
def createSession(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Session")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        if execution['success']:
            response = execution['data']
        else:
            response = execution
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createPharmacy(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Pharmacy")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        if execution['success']:
            response = execution['data']
        else:
            response = execution
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createPatient(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Patient")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        if execution['success']:
            response = execution['data']
        else:
            response = execution
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createBasket(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Basket")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        if execution['success']:
            response = execution['data']
        else:
            response = execution
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createDrug(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Drug")
    ids = []
    for child in objects['drugs']:
        activity = Activity("Drug")
        try:
            execution = activity.create(**child)
        except Exception as e:
            response = {'success':False,'message':str(e)}
            dump = json.dumps(response,cls=ExtendedEncoder)
            return HttpResponse(dump, content_type='application/json')
        else:
            if execution['success']:
                ids.append(execution['data'])
            else:
                response = execution
                dump = json.dumps(response,cls=ExtendedEncoder)
                return HttpResponse(dump, content_type='application/json')
    response = {}
    response['success'] = True
    response['message'] = "Successful"
    response['data'] = ids
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')



@csrf_exempt
def createParent(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Parent")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        response = execution
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')



@csrf_exempt
def createChildren(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val

    ids = []
    for child in objects['children']:
        activity = Activity("Child")
        try:
            execution = activity.create(**child)
        except Exception as e:
            response = {'success':False,'message':str(e)}
            dump = json.dumps(response,cls=ExtendedEncoder)
            return HttpResponse(dump, content_type='application/json')
        else:
            if execution['success']:
                ids.append(execution['data'])
            else:
                response = execution
                dump = json.dumps(response,cls=ExtendedEncoder)
                return HttpResponse(dump, content_type='application/json')
    response = {}
    response['success'] = True
    response['message'] = "Successful"
    response['data'] = ids
    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')



@csrf_exempt
def getParents(request):
    objs = Child.objects.all()
    objects = []
    for i in objs:
        # obj = {}
        # obj['parent']=i
        # obj['children'] = [i for i in i.children.all()]
        objects.append(i)
    data = {'success':True,'objects':objects}
    dump = json.dumps(data,sort_keys=True,indent=4,cls=ExtendedEncoderAllFields)
    newfile = open("/home/Learn/observe/campaigns/templates/{}.json".format("kpehe"),'w+')
    newfile.write(dump)
    newfile.close()
    json2csv("kpehe")
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createInn(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val
    activity = Activity("Inn")
    try:
        execution = activity.create(**objects)
    except Exception as e:
        response = {'success':False,'message':str(e)}
    else:
        if execution['success']:
            response = execution['data']
        else:
            response = execution

    dump = json.dumps(response,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')


@csrf_exempt
def createDrugReference(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    for key,val in json_data.items():
        objects[key]=val

    # initialize a new drugReference
    rf = drugReference()
    rf.brand_name = objects['brand_name']

    try:
        inn = Inn.objects.get(inn=objects['inn'])
    except:
        data = {'success':False}
    else:
        rf.save()
        rf.inn = inn
        data = {'success':True}
    rf.save()

    dump = json.dumps(data,cls=ExtendedEncoder)
    return HttpResponse(dump, content_type='application/json')





