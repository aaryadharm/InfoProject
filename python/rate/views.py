from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import os
# from config.definitions import ROOT_DIR
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "rate/index.html")

def course(request, coursename):
    cd = os.getcwd()
    reviews = pd.read_csv(os.path.join(cd, 'rate/reviews.csv')).to_dict('records')
    print(reviews)
    output = {}
    for review in reviews:
        if review['coursename'] == coursename:
            output[review['username']] = review['rating']

    return render(request, "rate/course.html", {
        "course": coursename.upper(),
        "reviews": output
    })