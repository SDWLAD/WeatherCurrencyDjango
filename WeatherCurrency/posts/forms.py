from .models import *
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("title", "text")

        widgets = {
            'title' : TextInput(attrs={"class":"title_input", "placeholder":"Введіть назву статті"}),
            'text' : Textarea(attrs={"rows":'5', "name":"text", "class":"text_input", "placeholder":'Напишіть текст статті'})
        }