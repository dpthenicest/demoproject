from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
  return HttpResponse(f"""
    <h3>404: Page Not Found</h3>
    <a href=''>Go to Home Page</a>
      """)

def home(request):
  return HttpResponseNotFound("Little Lemon!")