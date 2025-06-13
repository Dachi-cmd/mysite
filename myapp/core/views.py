from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def venus(request):
    return render(request, 'venus.html')

from django.shortcuts import render, get_object_or_404
from .models import Planet

def planet_detail(request, name):
    planet = get_object_or_404(Planet, name__iexact=name)
    return render(request, 'index.html', {'planet': planet})

