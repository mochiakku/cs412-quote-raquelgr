from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

quotes = ["Life is like a game: sometimes you win, sometimes you lose, but you always have to keep playing.",
          "It doesn't matter how many times you fall, what matters is getting up and moving forward.",
          "Humor is the best way to face life.",
          "Doing what you love is the key to happiness.",
          "There's always a new level to reach; never get stuck."]

images = ["https://static.wikia.nocookie.net/youtubepedia/images/4/47/Alexelcapo_1.PNG/revision/latest?cb=20200214201549&path-prefix=es",
        "https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2022/10/alexelcapo-2856489.jpg?tf=1200x1200",
        "https://pbs.twimg.com/media/Cv3mRpnXYAAbh-3.jpg:large",
        "https://cdn.beahero.gg/2022/08/Chio-Alexelcapo-Ruptura.jpg",
        "https://pm1.aminoapps.com/6704/c9ba921560d32eb10dd7503a62f3bdb1c3b98541_hq.jpg"]


def quote (request):
    # A function to respond to the /quotes url

    template_name = "quotes/quote.html"
    context = {
        "quote": random.choice(quotes),
        "image": random.choice(images),
        "current_time": time.ctime(),
    }
    return render(request, template_name, context)

def show_all(request):
    #A function to respond to the /quotes/show_all url
    template_name = "quotes/show_all.html"
    context = {
        "quotes": quotes,
        "images": images,
        "current_time": time.ctime(),
    }
    return render(request, template_name, context)

def about(request):
    template_name = "quotes/about.html"
    context = {
        "current_time": time.ctime(),
    }
    return render(request, template_name, context)
