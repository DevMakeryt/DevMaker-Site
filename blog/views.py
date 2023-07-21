from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.db.models import F

from django.db.models import Q

from core.models import UserProfile
from .models import Post
from django.views.generic.list import ListView


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.order_by('-created')[:20]
        ordered_posts = sorted(posts, key=lambda post: post.views, reverse=True)[:3]
        context['posts'] = posts
        context['posts_highlights'] = ordered_posts
        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class TeamView(TemplateView):
    template_name = 'blog/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        object, null = Group.objects.get_or_create(name='team')

        team = object.user_set.all()

        context['team'] = team

        return context


class TeamProfileView(DetailView):
    model = UserProfile
    template_name = 'blog/team_profile.html'
    context_object_name = 'profile'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('search')

        if search_query:
            queryset = queryset.filter(
                Q(content__icontains=search_query) |
                Q(title__icontains=search_query)
            )



        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        # Atualiza o contador de visualizações quando o post for acessado
        post = super().get_object(queryset=queryset)
        post.views += 1
        post.save()
        return post
