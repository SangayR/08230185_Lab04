from django.shortcuts import render
from .models import LearningJourney

def index(request):
    journeys = LearningJourney.objects.all().order_by('-date')
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    return render(request, 'aboutMe.html')
