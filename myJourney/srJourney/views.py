from django.shortcuts import render
from .models import LearningJourney, AboutMe

def index(request):
    journeys = LearningJourney.objects.all().order_by('-date')
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    about = AboutMe.objects.first()  # fetch the first AboutMe entry
    return render(request, 'aboutMe.html', {'about': about})  # pass the instance
