from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Idea
from .forms import IdeaForm

# Create your views here.

class IdeaList(generic.ListView):
    queryset = Idea.objects.all().order_by('-created_on')
    template_name = "forum/index.html"


def idea_detail(request, slug):
    queryset = Idea.objects.all()
    idea = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "forum/idea_detail.html",
        {
            "idea": idea,
            "idea_form": idea_form,

        },
    )

def idea_form(request):

    # Create the form first
    form = IdeaForm()

    return render(
        request,
        "forum/idea_form.html",
        {
            "idea_form": form,
        }
    )