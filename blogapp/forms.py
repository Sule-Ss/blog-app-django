from django import forms
from .models import Blog

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