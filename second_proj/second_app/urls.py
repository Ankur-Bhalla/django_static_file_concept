# include() on project urls.py functions

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # called from project urls.py and now call function index on views.py
]
