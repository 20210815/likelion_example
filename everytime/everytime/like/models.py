from django.db import models
from user.models import User
from board.models import Post

# Create your models here.
class PostLike(models.Model):
  user = models.ForeignKey(User, related_name= 'post_like_user', on_delete=models.CASCADE)
  post = models.ForeignKey(Post, related_name="post_like", on_delete=models.CASCADE)