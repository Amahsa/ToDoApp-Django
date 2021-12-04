from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from django.views.generic import DetailView,ListView

# ---------------------------------------    

def home_page(req):
    last3 = Todo.objects.all().order_by('-id')[:3]

    mydictionary = {
        'todo' : last3  
    }
    print(mydictionary)
    return render(req,'todoapp/home_page.html' , context = mydictionary )
# ---------------------------------------    

def add_task(request):
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary = {
        'todo' : last3  
    }
    return render(request,'todoapp/add_task.html' ,context = mydictionary)
# ---------------------------------------    

def submit(request):
    obj = Todo()
    cat = Category()
    cat.category_name = request.GET['category']
    if not Category.objects.filter(category_name__contains = request.GET['category'] ):
        cat.save()
    obj.title = request.GET['title']
    obj.category = Category.objects.filter(category_name__contains = request.GET['category'] )[0]
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.Scheduling = request.GET['scheduling']   
    obj.save()
    last3 = Todo.objects.all().order_by('-id')[:3]

    mydictionary = {
        "alltodos" : Todo.objects.all(),
        'todo' : last3 
    }
    print(mydictionary)
    return render(request,'todoapp/add_task.html',context=mydictionary)
# ---------------------------------------    

def details(request,id):
    obj = Todo.objects.get(id=id)
    last3 = Todo.objects.all().order_by('-id')[:3]

    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "category" : obj.category,
        "priority" : obj.priority,
        "created_at" : obj.created_at,
        "scheduling" : obj.Scheduling,
        "id" : obj.id,
        'alltodos' :  obj,
        'todo' : last3 
    }
    return render(request,'todoapp/todo_detail.html',context=mydictionary)
# ---------------------------------------    

# class todoDetail(DetailView):
#     model = Todo
# ---------------------------------------    

# def list(request):
#     mydictionary = {
#         "alltodos" : Todo.objects.all()
#     }
#     return render(request,'todoapp/todo_list.html',context=mydictionary)


# ---------------------------------------    

class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = Todo.objects.all().order_by('-id')[:3]
        return context
# ---------------------------------------    

def category_tasks(req,id):
    last3 = Todo.objects.all().order_by('-id')[:3]

    mydictionary = {
       'todos' : Todo.objects.filter(category = id ),
       'todo' : last3  
    }
    
    return render(req,'todoapp/category_tasks_list.html',context=mydictionary)

# ---------------------------------------    

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary = {
        "alltodos" : Todo.objects.all(),
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    

def list(request):
    all_todos = Todo.objects.all()
    last3 = Todo.objects.all().order_by('-id')[:3]

    mydictionary = {
        "alltodos" : all_todos,
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    

def sortdata_by_scheduling(request):
    
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-Scheduling'),
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    
def sortdata_by_id(request):
    
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-id'),
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    
def sortdata_by_priority(request):
    
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('priority'),
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    
def searchdata(request):
    last3 = Todo.objects.all().order_by('-id')[:3]  
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q),
        'todo' : last3 
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    

def update(request,id):
    obj = Todo(id=id)
    previuse_obj = Todo.objects.get(id = id)
    # print('ssssss',previuse_obj.created_at)
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    obj.Scheduling = request.POST['Scheduling']
    

    cat = Category()
    cat.category_name = request.POST['category']
    if not Category.objects.filter(category_name__contains = request.POST['category'] ):
        cat.save()

    obj.category = Category.objects.filter(category_name__contains = request.POST['category'] )[0]

    
    # import datetime
    # updated_at = datetime.datetime.now()
    obj.created_at = previuse_obj.created_at
    # print('new updated_at : ', obj.created_at)
    obj.save()
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary = {
        "alltodos" : Todo.objects.all(),
        'todo' : last3 ,
    }
    return render(request,'todoapp/todo_list.html',context=mydictionary)
# ---------------------------------------    
def edit(request,id):
    last3 = Todo.objects.all().order_by('-id')[:3]
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id,
        "category" : obj.category,
        "Scheduling" : str(obj.Scheduling.strftime('%Y-%m-%d')),
        'todo' : last3 
    }
    # print('ddddddddd',obj.Scheduling.strftime('%m/%d/%Y'))
    return render(request,'todoapp/edit.html',context=mydictionary)

# ------------------------------------------------
def category_delete(request,id):
    obj = Category.objects.get(id=id)
    obj.delete()
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary = {
        "alltodos" : Todo.objects.all(),
        'todo' : last3 ,
    }
    return render(request,'todoapp/category_list.html',context=mydictionary)
# -------------------------------------------------
def category_edit(request,id):
    obj = Category.objects.get(id=id)
    # obj.delete()
    last3 = Todo.objects.all().order_by('-id')[:3]
    mydictionary = {
        "alltodos" : Todo.objects.all(),
        'todo' : last3 ,
        "id" : obj.id,
        "category_name" : obj.category_name,
        
    }
    return render(request,'todoapp/category_edit.html',context=mydictionary)

# -----------------------------------------------
def category_update(request,id):
   
    Category.objects.filter(id = id).update(category_name=request.POST['category_name'])
 
    mydictionary = {
        
        'todo' : Todo.objects.all().order_by('-id')[:3] ,
        "category_list" : Category.objects.all(),
    }
    print('mydictionary : ' , mydictionary)
    return render(request,'todoapp/category_list.html',context=mydictionary)

