from django import forms
from .models import Category, Post

class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título del post'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenido'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control', 'placeholder':'Autor'}),
            'categories' :forms.CheckboxSelectMultiple(),
        }