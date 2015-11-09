from django import forms

from apps.posts.models import Post

class PostForm(forms.ModelForm):
    """docstrings for PostForm"""

    class Meta:
        model = Post
        fields = ('id', 'name', 'slug', 'description', 'videoDurationFe', 'externalView',
                    'category')

        widgets = {
            'category': forms.widgets.Select(
                                    attrs={'class': 'form-control select2'}) 
        }