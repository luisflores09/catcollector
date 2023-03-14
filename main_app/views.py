from django.shortcuts import render

# Create your views here.


def home(request):
    # Include an .html file extension
    return render(request, 'home.html')
