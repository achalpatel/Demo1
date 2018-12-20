from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import datetime
from shopping.forms import CategoryForm,ProductForm
from shopping.models import Category, Product
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, "welcome.html",{})


def category_index(request):
    context = {}
    context['cat'] = Category.objects.all()
    return render(request,"dashboard.html", context)


def admin_dashboard(request):
    context = {}
    context['cat'] = Category.objects.all()
    return render(request, "dashboard.html", context)


def create_category(request):
    context={}
    if request.method == 'GET':
        form = CategoryForm()
    elif request.method == 'POST':
        form = CategoryForm(data = request.POST)
        if form.is_valid():
            cat = form.save()
            return HttpResponseRedirect('/shopping/admin_dashboard')
    context['form'] = form
    return render(request, 'category_create.html', context)

def edit_category(request):
    context = {}
    if request.method == 'GET' and 'catid' in request.GET:
        cid = request.GET['catid']
        context['catid'] = cid
        instance = Category.objects.get(catid = cid)
        form = CategoryForm(instance = instance)
    elif request.method == 'POST':
        cid = request.POST['catid']
        instance = Category.objects.get(catid = cid)
        form = CategoryForm(data = request.POST, instance = instance)
        if form.is_valid():
            cat = form.save()
            return HttpResponseRedirect('/shopping/admin_dashboard')
    else:
        return HttpResponse("Category Id is mandatory")
    context['form']= form
    return render(request, 'category_create.html', context)

def delete_category(request):
    context = {}
    if request.method == 'GET' and 'cid' in request.GET:
        cid = request.GET['cid']
        context['cid'] = cid
        instance = Category.objects.get(catid=cid)
        form = CategoryForm(instance=instance)

    elif request.method == "POST":
        cid = request.POST['catid']
        instance = Category.objects.get(catid=cid)
        if form.is_valid():
            messages.success(request, "Catergory <strong>%s</strong> is Deleted "%instance.cname)
            instance.delete()
            return HttpResponseRedirect('/users/category_index/')
    else:
        return HttpResponse("Category id is mandaory")

    context['form'] = form
    return render(request, 'category_delete.html', context)

def Product_index(request):
    context = {}
    context['pro'] = Product.objects.all()
    return render(request, "Product_index.html", context)

def create_product(request):
    context = {}
    if request.method == 'GET':
        form = ProductForm()
    elif request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"New Product is added Sucessfully")
            return HttpResponseRedirect('/shopping/Product_index/')
    context['form'] = form
    return render(request, 'product_create.html', context)

def edit_product(request):
    context = {}
    if request.method == 'GET' and 'pid' in request.GET:
        pid = request.GET['pid']
        context['pid'] = pid
        instance = Product.objects.get(pid=pid)
        form = ProductForm(instance=instance)

    elif request.method == "POST":
        pid = request.POST['pid']
        instance = Product.objects.get(pid=pid)
        form = ProductForm(data=request.POST, instance=instance,files=request.FILES)
        if form.is_valid():
            pro = form.save()
            messages.success(request,"Produt %s is updated Sucessfully"%pro.pname)
            return HttpResponseRedirect('/shopping/Product_index/')
    else:
        return HttpResponse("Product id is mandaory")
    context['form'] = form
    return render(request, 'product_create.html', context)

def delete_product(request):
    context = {}
    if request.method == 'GET' and 'pid' in request.GET:
        pid = request.GET['pid']
        context['pid'] = pid
        instance = Product.objects.get(pid=pid)
        form = ProductForm(instance=instance)

    if request.method == "POST":
        pid = request.POST['pid']
        instance = Product.objects.get(pid=pid)

        #if form.is_valid():
        messages.success(request, "Product <strong>%s</strong> is Deleted "%instance.pname)
        instance.delete()
        return HttpResponseRedirect('/shopping/Product_index/')
    else:
        return HttpResponse("Product id is mandaory")

    context['form'] = form
    return render(request, 'product_delete.html', context)
