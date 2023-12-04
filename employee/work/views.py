from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm,BookForm,DetailsForm,StudentsForm
from work.models import Emp,Book,Details,Students

# Create your views here
class Employee(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=EmpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
###
class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            #Book.objects.create(**form.cleaned_data)
#form.save() :method is used to add the data into database without using orm query (only for modelform)          
            form.save()
            print("created")
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
class Booklist(View):
    def get(self,request):
        qs=Book.objects.all()
        return render(request,"booklist.html",{"data":qs})
###

class DetailsView(View):
    def get(self,request):
        form=DetailsForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=DetailsForm(request.POST)
        if form.is_valid():          
            form.save()
            print("created")
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})

class Detailslist(View):
    def get(self,request):
        qs=Details.objects.all()
        return render(request,"details.html",{"data":qs})
class DetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Details.objects.get(id=id)
        return render (request, "details1.html",{"data":qs})
    
class StudentsView(View):
    def get(self,request):
        form=StudentsForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=StudentsForm(request.POST)
        if form.is_valid():          
            form.save()
            print(form.cleaned_data)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
        
class Book_detailView(View):
    def get(self,request,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render (request,"bookid.html",{"data":qs})
    
class Book_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Book.objects.get(id=id).delete()
        return redirect("book-al")

       

