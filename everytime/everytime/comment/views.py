from django.shortcuts import render
from board.models import Post
from .models import Comment

# Create your views here.

# def com_list(request, id):
#   #id는 post id
#   post = Post.objects.get(pk=id)
#   comments = Comment.objects.get(post=post)

#   return redirect