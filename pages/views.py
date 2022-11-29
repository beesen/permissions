from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def home_view(request: WSGIRequest):
    # user is
    user = request.user
    # group permissions
    menu_list = []
    menu = {
        'href': '/',
        'title': 'Home'
    }
    menu_list.append(menu)
    context = {
        'menu_list': menu_list
    }
    return render(request, 'pages/home.html', context)

def superuser_toggle_view(request: WSGIRequest):
    # switch superuser
    user = request.user
    user.is_superuser = not user.is_superuser
    user.save()
    return render(request, 'pages/home.html', context={})