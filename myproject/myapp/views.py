from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
  return HttpResponse('Hello, World!')

def display_date(request):
  date_joined = datetime.today()
  return HttpResponse(date_joined)

def menu(request):