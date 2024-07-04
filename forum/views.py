from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
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
def idea_edit(request, slug, idea_id):
    """
    view to edit idea
    """
    if request.method == "POST":

        idea = get_object_or_404(Idea, pk=idea_id)
        form = IdeaForm(data=request.POST, instance=idea)

        if form.is_valid() and idea.author == request.user:
            idea = form.save(commit=False)
            print('form in progress')
            idea.author = request.user
            idea.save()
            print('idea saved')
            messages.add_message(
                request, messages.SUCCESS,
                'Idea updated successfully!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating Idea!')
            return HttpResponseRedirect(reverse('idea_detail', args=[slug]))
    else:
        form = IdeaForm()

    return HttpResponseRedirect(reverse('home'))

# @login_required
def idea_delete(request, slug, idea_id):
    """
    view to delete idea
    """
    idea = get_object_or_404(Idea, pk=idea_id, slug=slug)

    if idea.author == request.user:
        idea.delete()
        messages.add_message(request, messages.SUCCESS, 'Idea deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own ideas!')

    return HttpResponseRedirect(reverse('home'))


# @login_required
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

    return HttpResponseRedirect(reverse('idea_detail', args=[slug]))


# @login_required
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Idea.objects.all()
    idea = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('idea_detail', args=[slug]))