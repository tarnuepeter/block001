from django import forms 
from .models import Post, Comment 


class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'body', 'image', 'trending']


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        max_length=500, 
        widget=forms.Textarea(attrs={'class': 'form-control', "rows": 3, "placeholder": "Join the discussion and leave a comment!"})
    )
    class Meta: 
        model = Comment
        fields = ['body',]