from django import forms
from .models import Post

class VideoForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["name", "videofile"]