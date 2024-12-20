from django import forms
from blogapp.models import Blog

#create your forms here.

class BlogForm(forms.ModelForm):
    class Meta:
       model = Blog
       fields = "__all__"
       
       