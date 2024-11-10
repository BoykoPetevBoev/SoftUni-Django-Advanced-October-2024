from django import forms
from django_advanced.post_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'image_url': 'Post Image URL',
        }


class CreatePostForm(PostForm):
    class Meta(PostForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
            'image_url': forms.TextInput(attrs={'helptext': 'Share your funniest furry photo URL!'}),
        }


class EditPostForm(PostForm):
    class Meta(PostForm.Meta):
        help_texts = {
            'image_url': None
        }


class DeletePostForm(PostForm):
    class Meta(PostForm.Meta):
        help_texts = {
            'image_url': None
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.widget.attrs['readonly'] = "readonly"


class SearchForm(forms.Form):
    class Meta():
        fields = "__all__"
    
    post_title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by post tile...',
            }
        )
    )