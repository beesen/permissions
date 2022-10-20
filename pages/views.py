from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def home_view(request: WSGIRequest):
    return render(request, 'pages/home.html', context={})