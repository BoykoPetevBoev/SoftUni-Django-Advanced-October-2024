from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django_advanced.post_app.models import Post
from django_advanced.post_app.forms import CreatePostForm, EditPostForm, DeletePostForm, SearchForm
from django_advanced.user_app.models import CustomUser
from django_advanced.user_app.mixins import AuthorMixin


class DetailsPostPage(AuthorMixin, DetailView):
    model = Post
    template_name = 'post/details-post.html'


class ListPostPage(AuthorMixin, ListView):
    model = Post
    template_name = 'post/list-post.html'
    context_object_name = 'posts'
    paginate_py = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        post_title = self.request.GET.get('post_title')
        if post_title:
            queryset = queryset.filter(title__icontains=post_title)
        return queryset


class CreatePostPage(AuthorMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.author = CustomUser.objects.first()
        return super().form_valid(form)


class EditPostPage(AuthorMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('posts')


class DeletePostPage(AuthorMixin, DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('posts')
    
    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)