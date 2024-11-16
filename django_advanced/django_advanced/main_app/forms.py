# from django import forms
# from django_advanced.main_app.models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ["text"]
#         widgets = {
#             'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
#         }


# class SearchForm(forms.Form):
#     class Meta():
#         fields = "__all__"
    
#     post = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Search by title...',
#             }
#         )
#     )
