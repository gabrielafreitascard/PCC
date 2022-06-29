
from django.forms import ModelForm
from .models import Image, Post

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('titulo', 'conteudo','image')