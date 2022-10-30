# _*_ coding: utf-8 _*_

from django import forms

from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'