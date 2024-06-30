from .models import Idea
from django import forms


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'purpose', 'mockup_image', 'details', 'issues', 'progress')