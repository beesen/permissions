from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def home_view(request: WSGIRequest):
    return render(request, 'pages/home.html', context={})

def superuser_toggle_view(request: WSGIRequest):
    # switch superuser
    user = request.user
    user.is_superuser = not user.is_superuser
    user.save()
    return render(request, 'pages/home.html', context={})