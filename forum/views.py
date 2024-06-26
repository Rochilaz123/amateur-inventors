from django.shortcuts import render
from django.views import generic
from.models import Idea

# Create your views here.

class IdeaList(generic.ListView):
    queryset = Idea.objects.all().order_by('-created_on')
    template_name = "forum/index.html"