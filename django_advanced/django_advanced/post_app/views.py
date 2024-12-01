from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from django_advanced.post_app.forms import (CreatePostForm, DeletePostForm, EditPostForm, SearchForm, CommentForm)
from django_advanced.post_app.models import Post, Like, Comment
from django_advanced.post_app.serializers import PostSerializer
from django_advanced.user_app.mixins import AuthorMixin

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema


@extend_schema(
    request=PostSerializer,
    responses={201: PostSerializer, 400: PostSerializer},
)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailsPostPage(DetailView):
    model = Post
    template_name = 'post/details-post.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['author'] = post.author
        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context


class ListPostPage(ListView):
    model = Post
    template_name = 'post/list-post.html'
    context_object_name = 'page_obj '
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        post_title = self.request.GET.get('post')
        if post_title:
            queryset = queryset.filter(title__icontains=post_title)
        return queryset


class CreatePostPage(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user.profile
        return super().form_valid(form)
    

class EditPostPage(LoginRequiredMixin, AuthorMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('posts')


class DeletePostPage(LoginRequiredMixin, AuthorMixin, DeleteView):
    model = Post
    form_class = DeletePostForm
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('posts')
    
    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
    
    
    
@login_required
def likes_functionality(request, pk: int):
    if request.POST:
        like = Like.objects.get(
            post_id=pk,
            user=request.user.profile
        )

        if like:
            like.delete()
        else:
            like = Like(post_id=pk, user=request.user.profile)
            like.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{pk}')


@login_required
def comment_functionality(request, pk: int):
    if request.POST:
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user.profile
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{pk}')