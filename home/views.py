from django.http import HttpResponse 
from django.shortcuts import render
from django.http import HttpResponse

from .forms import bookingforms

from .models import departments,doctors

# Create your views here.
def index(request):

    numbers = {
        'fruits':['banana','apple','grapes',]

    }
    return render(request,'index.html', numbers)

def about(request):
    return render(request,'about.html',dict_forms)
    
def booking(request):
    if request.method == "POST":
        form = bookingforms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = bookingforms()
    dict_form={
        'form':form
    }
    return render(request,'booking.html', dict_form)

def doctor(request):
    dict_docs= {
        'doctors': doctors.objects.all()
    }
    return render(request,'doctors.html', dict_docs)


def contact(request):
    return render(request,'contact.html')


def department(request):
    dict_dept ={
        'dept':departments.object.all()
    }
    return render(request,'department.html', dict_dept)

