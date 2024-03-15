from django.db import models
from user.models import User
from board.models import Post

# Create your models here.
class Comment(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
  created_at = models.DateTimeField(auto_now_add=True)
  anonymity = models.BooleanField(default=True)