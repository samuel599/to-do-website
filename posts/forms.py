from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','description','datetime']

    datetime = forms.DateTimeField(
        input_formats = ['%Y-%m-%d %H:%M:%S'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
