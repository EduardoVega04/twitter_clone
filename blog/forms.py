from django import forms
from .models import Post


class PostCreation(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'media']
        widgets = {
            'content': forms.Textarea(attrs={
                'required': False,
                'placeholder': "What's happening?",
                'rows': 2
            }),
            'media': forms.FileInput(attrs={
                'accept': 'image/jpeg, image/png, image/webp, image/gif, video/mp4, video/quicktime, video/webm'
            })
        }
