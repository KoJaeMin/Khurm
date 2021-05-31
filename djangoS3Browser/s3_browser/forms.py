from django import forms
from folder.models import File

class PostForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'