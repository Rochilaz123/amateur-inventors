from .models import Idea, Comment
from django import forms


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'purpose', 'mockup_image', 'details', 'issues', 'progress')

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)