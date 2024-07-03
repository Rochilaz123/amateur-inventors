from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Idea, Comment
from .forms import IdeaForm, CommentForm

# Create your views here.

class IdeaList(generic.ListView):
    queryset = Idea.objects.all().order_by('-created_on')
    template_name = "forum/index.html"


def idea_detail(request, slug):
    queryset = Idea.objects.all()
    idea = get_object_or_404(queryset, slug=slug)
    comments = idea.comments.all().order_by("-created_on")
    comment_count = idea.comments.all().count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.idea = idea
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted successfully!'
                )

    comment_form = CommentForm()
    # This was not added - you will also need to add the post functionality here -
    # essentially you are staying in the detail view when you are clicking on the modal 
    idea_form = IdeaForm()
    return render(
        request,
        "forum/idea_detail.html",
        {
            "idea": idea,
            "idea_form": idea_form,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
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


# @login_required
def idea_edit(request):
    idea = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        if form.is_valid() and idea.author == request.user:
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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Idea.objects.all()
        idea = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.idea = idea
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect('/', 'slug=slug')
    # return HttpResponseRedirect(reverse('idea_detail', args=[slug]))