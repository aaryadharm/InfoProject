from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "rate/index.html")

def course(request, coursename):
    return render(request, "rate/course.html", {
        "course": coursename.upper()
    })