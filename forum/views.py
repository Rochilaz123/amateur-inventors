from django.shortcuts import render
from django.views import generic
from.models import Idea

# Create your views here.

class IdeaList(generic.ListView):
    queryset = Idea.objects.all()
    template_name = "idea_list.html"