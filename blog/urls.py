
from django.urls import path, include

from blog.views import HomeView, PostListView, PostDetailView, AboutView, TeamView, TeamProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('team', TeamView.as_view(), name='team'),
    path('team/profile/<slug:slug>', TeamProfileView.as_view(), name='team_profile'),
    path('post/list', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),

]

