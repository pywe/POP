from django.shortcuts import render,redirect,HttpResponse
import json
# from tastypie.models import ApiKey
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from campaigns.models import *

# Create your views here.
def index(request):
    template_name = "accounts/campaign_list.html"
    args = {}
    # if request.user.is_authenticated:
    return render(request,template_name,args)
    # else:
    # return redirect('login')


def new_session(request):
    template_name = "accounts/new_session.html"
    args = {}
    # if request.user.is_authenticated:
    return render(request,template_name,args)


# Login page for users visiting with browser
def login_view(request):
    template_name = "accounts/login.html"
    args = {}
    return render(request,template_name,args)


# Login a user through api call
@csrf_exempt
def api_login(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    username = json_data['username']
    password = json_data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # login(request, user)
        # Redirect to a success page.
        # messages.success(request, "Login success")
        # return render(request,template_name,args)
        myuser = {}
        myuser['username']=user.username
        myuser['id']=user.id
        myuser['email']=user.email
        myuser['active']=user.is_active
        data = {'success':True,'message':'Successfully logged in',"user":myuser}
    else:
        data = {'success':False,'message':'Could not find user'}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


# Fetch campaign list for user
@csrf_exempt
def fetch_campaigns(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    mycountry = json_data['country']
    try:
        country = Country.objects.get(name=mycountry)
    except:
        data = {'success':False,'objects':[]}
    else:
        campaign_list = Campaign.objects.filter(country=country)
        objects = []
        for campaign in campaign_list:
            obj = {}
            obj['name']=campaign.name
            obj['id']=campaign.id
            obj['status']=campaign.status
            obj['country']=campaign.country.name
            objects.append(obj)
        data = {'success':True,'objects':objects}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')




