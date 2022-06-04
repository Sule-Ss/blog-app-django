from django import forms
from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields= ["title","content","image","category","status"]
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'category': 'Category',
            'status': 'Status',
        }

        widgets = {
            'content': forms.Textarea(attrs={'cols':40, 'rows':10})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)