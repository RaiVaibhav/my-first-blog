from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    def __init__(self, **kwargs):
        self.author = kwargs.pop('author', None)
        super(CommentForm, self).__init__(**kwargs)

    def save(self, commit):
        obj = super(CommentForm, self).save(commit=False)
        obj.author = self.author.username
        if not obj.author:
            obj.author = 'Anonymous'
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Comment
        fields = ('text',)
