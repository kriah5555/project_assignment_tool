from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employees,Project,ProjectAssignment1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import error




user = object()

# Create your views here.
def intex_page(request):
    return render(request, 'index.html')

#authenticate login and go to home page
def login_authentication(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
        # global user
        # user = Employees.objects.get(username = request.POST['username'], password = request.POST['password'] )
        context = {'users':Employees.objects.all()}
        return render(request, 'mainpage.html',context)

#same as login page with employee list
@login_required
def home_page(request):
    global user
    #user = Employees.objects.get(username = request.POST['username'], password = request.POST['password'] )
    #print('++++++++++++++++++',Employees._meta.fields)
    context = {'users':Employees.objects.all()}
    return render(request, 'mainpage.html',context)

def logoutu(request):
    # global user 
    # user = None
    logout(request)
    return render(request, 'index.html')
    
#all employees detaile page
def detail_view(request):
    global user 
    if request.method == 'POST':
        context = {'users':Employees.objects.filter(name__icontains  = request.POST['search_employee'])}
    elif request.method == 'GET':
        context = {'users':Employees.objects.all()}

    #will get all the column names
    for i in Employees._meta.fields:
            print(i.name)
    
    return render(request, 'detail_view.html',context)

#Project list page
def project_list_page(request):
    if request.method == 'POST' :
        #print('-------------',request.POST['search_project'])
        #Filter which will search for all the names sub strian and case insensetive
        context = {'projects':Project.objects.filter(project_name__icontains = request.POST['search_project'])}
    else:
        context = {'projects':Project.objects.all()}
    return render(request, 'project_list.html',context)

#add project
def add_project(request):
    return render(request, 'add_project.html')

#Assign project to employee
def addproject(request):
    st = ''
    if Project.objects.filter(project_name = request.POST['project_name']).count()==0:
        Project.objects.create(project_name = request.POST['project_name'], projedct_start_time = request.POST['projedct_start_time'], project_end_time = request.POST['project_end_time'])
        return redirect('/project_list_page/',{'status : st'})
    else:
        st = ''
        return redirect('/project_list_page/')

#assign project after clicking on project page
def assign_project(request,project_name):
    st = ''
    if request.method == 'POST':
        employee_name = request.POST['selectedvlauehh']
        #check if project alreday assigned to the employee
        if ProjectAssignment1.objects.filter(project_name = project_name).filter(employee_name = employee_name).count()==0: 
            st = 'Project asigned successfully'
            p = ProjectAssignment1()
            p.project_name = project_name
            p.employee_name = employee_name
            p.save()
        else:
            st = f'Project already assigned to {employee_name}'
        employees = [j.name for j in Employees.objects.all()]
        return render(request, 'assign_project.html',{'employees':employees,'project_name':project_name,'status':st})

    elif request.method == 'GET':
        st = ''
        employees = [j.name for j in Employees.objects.all()]
        #print('----------------',project_name)
        return render(request, 'assign_project.html',{'employees':employees,'project_name':project_name,'status':st})

#employ details with projects
def employee_projects(request,employee_name):
    projects    = ProjectAssignment1.objects.all().filter(employee_name = employee_name)
    employee       = Employees.objects.get(name = employee_name)
    #print('--------------------',projects)
    return render(request, 'employ_detail_with_projects.html',{'employee':employee,'projects':projects})


