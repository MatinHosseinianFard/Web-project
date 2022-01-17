from django import forms
from django.forms import fields
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "text")


        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'name-comment', 'placeholder': 'نام شما'}),
            'text': forms.Textarea(attrs={'class': 'text-comment', 'placeholder': 'متن نظر. .'}),

        }

        # labels = {
        #     'name':  "نام شما",
        #     'text': "متن نظر",
        # }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ("title", "slug", "image", "body", "author", "tags", "category")
        exclude = ("date","visitors")

        widgets = {
            
            'author': forms.TextInput(attrs={'id': 'elder', 'type': 'hidden'}),
            'title': forms.TextInput(attrs={'class': 'title-post'}),
            'tags': forms.SelectMultiple(attrs={'class': 'tags-post'}),
            'category': forms.Select(attrs={'class': 'category-post'}),
            'promote': forms.CheckboxInput(attrs={'class': 'promote-post'}),
        }

        labels = {
            'title':  "عنوان",
            'body': "",
            'author': "",
            'tags': "تگ ها",
            'category': "دسته بندی",
            'promote': "قرار گرفتن در اسلایدر",
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "image", "body", "tags", "category")

        widgets = {
                'title': forms.TextInput(attrs={'class': 'title-post'}),
                'tags': forms.SelectMultiple(attrs={'class': 'tags-post'}),
                'category': forms.Select(attrs={'class': 'category-post'}),
            }

        labels = {
            'title':  "عنوان",
            'body': "",
            'tags': "تگ ها",
            'category': "دسته بندی",
        }