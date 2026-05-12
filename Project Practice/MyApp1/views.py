from django.shortcuts import render,  redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import InputForm
from .models import assessment
from .forms import InputForm2

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO

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



def report(request):
    pdf_file = staticfiles_storage .path("DS.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)
       
        response = FileResponse(buffer, as_attachment=True, filename="noAttachment.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="noAttachment.pdf")

    return response


def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.name, teach.area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new user with hashed password
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'MyApp1/signup.html', {'form': form})

def home2(request):
    return render(request, 'MyApp1/home2.html')
