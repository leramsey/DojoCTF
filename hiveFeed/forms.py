from django import forms
from .models import hivePost

class postCreateForm(forms.ModelForm):
    class Meta:
        model = hivePost
        fields = [ 'post_title',
                   'post_body',
                   'post_author',
                   ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-rounded', 'placeholder': 'title...'}),
            'body': forms.TextInput(attrs={'class': 'textarea has-fixed-size', 'placeholder': 'Post Body'}),
        }