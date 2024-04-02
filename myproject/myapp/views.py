from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .forms import InputForm, LogForm

# Create your views here.
def home(request):
  return HttpResponse('Hello, World!')

def display_date(request):
  date_joined = datetime.today()
  return HttpResponse(date_joined)

def menu(request):
  content = "<h1>Menu:</h1><p>Salad</p><p>Bread</p>"
  return HttpResponse(content)

def path(request):
  path = request.path
  response = HttpResponse(path, content_type="text/html", charset = 'utf-8')
  return response

def request_info(request):
  path = request.path
  scheme = request.scheme
  method = request.method
  address = request.META['REMOTE_ADDR']
  user_agent= request.META['HTTP_USER_AGENT']
  path_info = request.path_info

  response = HttpResponse()
  response.headers['Age'] = 20

  msg = f"""<br>
    <br>Path: {path}
    <br>Address: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User Agent: {user_agent}
    <br>Path Info: {path_info}
    <br>Response Headers: {response.headers}
  """
  
  content = HttpResponse(msg, content_type = 'text/html', charset = 'utf-8')
  return content

def menuitems(request, dish):
  items = {
    'pasta': 'Pasta is a type of noodle made from combination of wheat, water or eggs.',
    'falafel': 'Falafel are deep fried patties or balls made from',
    'cheesecake': 'Cheesecake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce topping.'
    }
  
  description = items[dish]

  return HttpResponse(f"<h2>{dish} </h2> <p>{description}")

def form_view(request):
  form = InputForm()
  context = {"form": form}
  return render(request, "home.html", context)

def log_view(request):
  form = LogForm()
  if request.method == 'POST':
    form = LogForm(request.POST)
    if form.is_valid():
      form.save()
  context = {"form": form}
  return render(request, "log.html", context)