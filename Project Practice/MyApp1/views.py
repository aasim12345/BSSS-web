from django.shortcuts import render,  redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import InputForm
from .models import assessment
from .forms import InputForm2


# Create your views here.
def index(request):
    teach = teacher.objects.all()
    assign = assessment.objects.all()

    context = {
        'content2': assign,
        'content' : teach
        }
    return render(request,"MyApp1/index.html",context)

def input_view(request):

    if request.method == "POST":

        form = InputForm(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm()



    return render(request, "MyApp1/input.html", {"form": form})
def assign_view(request):

    if request.method == "POST":

        form = InputForm2(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm2()



    return render(request, "MyApp1/assign.html", {"form": form})
def home(request):
 return render(request,"MyApp1/home.html")