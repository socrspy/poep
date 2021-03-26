from django.shortcuts import render
from django.views import View 
from .models import  Post, UserProfile


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')

        context = {
            'post_list': posts,
        }

        return render(request, 'social/post_list.html', context)
# Create your views here.

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user' : user,
            'profile' : profile,
            'posts' : posts
        }

        return render(request, 'social/profile.html', context)
