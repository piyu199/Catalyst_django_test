from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib import auth,messages
from django.contrib.auth.models import User
import pandas as pd
from .models import FileUpload,Person
from querybuilder.query import Query


# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('file_upload')
        else:
            messages.info(request,"credential Invalid")
            return render(request,'index.html')
    return render(request,'index.html')

def create_db(file_path):
    df=pd.read_csv(file_path,delimiter=',')
    print(df.values)
    list_of_csv=[list(row) for row in df.values]

    for l in list_of_csv:
        Person.objects.create(
            id=l[0],
            name=l[1],
            domain=l[2],
            year_founded=l[3],
            industry=l[4],
            locality=l[6],
            country=l[7],
        )

@csrf_exempt
def file_upload(request):
    if request.method=='POST':
        file=request.FILES['file']
        # FileUpload.objects.create(file=file)
        fs=FileSystemStorage()
        file_path=fs.save(file.name,file)
        print(file_path)
        create_db(file_path=file)
        return HttpResponse("uploaded") 
    return render(request,'file_upload.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def display_user(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'display_user.html',context)

def query_builder(request):
    if request.method=='POST':
        domain=request.POST['domain']
        industry=request.POST['industry']
        locality=request.POST['locality']
        country=request.POST['country']
        query = Query().from_table({'my_table': Person}, [{'domain': domain}, {'industry': industry},{'locality':locality},{'country':country}])
        query.select()
        query.get_sql().count()
    return render(request,'query_builder.html')