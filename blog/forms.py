from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-field'}),
            # 'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-field'}),
            # 'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-field'})
        }
