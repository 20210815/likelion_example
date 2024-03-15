from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) #생성일자
  user = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE)
  anonymity = models.BooleanField(default="True")

  def __str__(self):
    return f'[{self.id}-{self.title}]'
  

#익댓 count
class ComCount(models.Model):
  user = models.ForeignKey(User, related_name="com_user", on_delete=models.DO_NOTHING)
  post = models.ForeignKey(Post, related_name="post_com", on_delete=models.CASCADE)
  order = models.PositiveIntegerField(default=0)

  def __str__(self):
        return f"ComCount #{self.order} for Post #{self.post.id}"