from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def kanyes_index(request):
    return render(request, 'kanyes/index.html', {'kanyes': kanyes})


class Kanye:
    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age


kanyes = [
    Kanye('Kanye East', 'from the eastside', 37),
    Kanye('Kanye West', 'college dropout era', 27),
    Kanye('Ye', 'kanye to ye', 44),
]
