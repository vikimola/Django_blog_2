from django.shortcuts import render
from .models import Post
import json
import urllib.request


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, "post.html", {"posts": posts})


def weather(request):
    if request.method == "POST":
        city = request.POST["city"]
        res = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f9868737066a6366b26f09f888eb6790").read()
        json_data = json.loads(res)
        data = {"coordinates": str(json_data["coord"]["lon"]) + " " + str(json_data["coord"]["lat"]),
                "country": json_data["sys"]["country"],
                "temp": str("{:.2f}".format(float(int(json_data["main"]["temp"]) - 273.85))),
                "pressure": str(json_data["main"]["pressure"]),
                "humidity": str(json_data["main"]["humidity"]),

                }


    else:
        city = ""
        data = {}

    return render(request, "Weather_app.html", {"city": city, "data":data})
