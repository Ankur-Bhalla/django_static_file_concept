# Static Media Files - for example, returning a User’s Photo

from django.shortcuts import render


# Create your views here.
def index(request):
    # my_dict = {"insert_me": "Render Message - Hello I am coming from views.py Enjoy image!"}
    # return render(request, "second_app/index.html", context=my_dict)
    return render(request, "second_app/index.html")
