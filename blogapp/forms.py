from django import forms
from .models import Blog
from .models import Comment

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields= '__all__'
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'category': 'Category',
            'status': 'Status',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols':80, 'rows':20})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)