from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Idea
from .forms import IdeaForm

# Create your views here.

class IdeaList(generic.ListView):
    queryset = Idea.objects.all().order_by('-created_on')
    template_name = "forum/index.html"


def idea_detail(request, slug):
    queryset = Idea.objects.all()
    idea = get_object_or_404(queryset, slug=slug)
    # This was not added - you will also need to ad the post functionality here - essentially you are staying in the detail view wheny ou are clicking on the modal 
    idea_form = IdeaForm()
    return render(
        request,
        "forum/idea_detail.html",
        {
            "idea": idea,
            "idea_form": idea_form,

        },
    )

# @login_required
def idea_form(request):

    # Create the form first
    form = IdeaForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for sharing your Idea!'
            )
            return HttpResponseRedirect('/')
    else:
        form = IdeaForm()
    
    return render(request, "forum/idea_form.html", {"idea_form": form})


# # @login_required
# def idea_edit(request, slug, idea_id):
#     """
#     view to edit ideas
#     """

#     if request.method == "POST":
#         queryset = Idea.objects.all()
#         idea = get_object_or_404(queryset, slug=slug)
#         form = IdeaForm(data=request.POST, instance=idea)

#         if form.is_valid() and idea.author == request.user:
#             idea = form.save(commit=False)
#             idea.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Idea successfully updated!'
#             )
#             return HttpResponseRedirect('/')
#         else:
#             messages.add_message(request, messages.ERROR,
#             'Error updating idea!')
    
#     return render(request, "forum/idea_form.html", {"idea_form": form})

# # @login_required
def idea_edit(request):
    idea = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Idea updated successfully!'
            )
            return HttpResponseRedirect('/')
    else:
        form = IdeaForm()
    return render(request, 'idea_detail.html', {'form': form, 'idea': idea})