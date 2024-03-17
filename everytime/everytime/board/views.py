from asyncio.windows_events import NULL
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, ComCount, Scrap, PostLike
from django.contrib.auth.decorators import login_required
from comment.models import Comment
from django.db.models import Count
from category.models import Category
from user.models import User
from django.db.models import F, ExpressionWrapper, fields
from django.utils import timezone
# Create your views here.

def list(request):
  posts = Post.objects.annotate(
        time=ExpressionWrapper(
            timezone.now() - F('created_at'),
            output_field=fields.DurationField()
        )
    ).order_by('-id')
  #posts = Post.objects.all().order_by('-id')
  
  # print(request.user.post_user.all())
  #posts = Post.objects.annotate(comment_count=Count('comment')).order_by('-id')
  return render(request, 'board/list.html', {'posts': posts})

def detail(request, id):
  post = get_object_or_404(Post, pk=id)
  comments = Comment.objects.filter(post = post)
  #해당 순서대로 번호 부여할 수 있도록....
  com_count = ComCount.objects.filter(post=post)
  return render(request, "board/detail.html", {'post': post, 'comments': comments, 'com_count': com_count})


@login_required
def create(request):
  if request.method == "POST":
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.content = request.POST['content']
    new_post.user = request.user
    print(request.POST.get('anonymity'))
    if request.POST.get('anonymity') == None:
      new_post.anonymity = False
      new_post.save()
    new_post.save()

    return redirect("board:list")
  return render(request, "board/create.html")

@login_required
def update(request, id):
  post = get_object_or_404(Post, pk=id)
  if request.method == "POST":
    post.title = request.POST['title']
    post.content = request.POST['content']

    post.save()
    return redirect("board:detail", post.id)
  elif request.method == "GET":
    return render(request, "board/update.html", {'post': post})
  

def delete(request,id):
  post = get_object_or_404(Post, pk=id)
  post.delete()
  return redirect("board:list")

@login_required
def com_create(request, id):
  if request.method == "POST":
    comment = Comment()
    comment.user = request.user
    comment.content = request.POST['content']
    comment.post = Post.objects.get(pk=id)
    if request.POST.get('anonymity') == None:
      comment.anonymity = False
    # 익명 카운트 부름
    comment.save()
    com_count(id, request)
    return redirect("board:detail", id)
  
def com_delete(request, com_id, post_id):
  post = Post.objects.get(pk=post_id)
  comment = Comment.objects.get(pk=com_id)
  comment.delete()

  return redirect("board:detail", post_id)


#댓글 익명 번호 관리
def com_count(post_id, request):
    # Get the currently logged-in user
    user = request.user
    post = Post.objects.get(pk=post_id)

    # Check if a ComCount instance already exists for the user and post
    com_count_exists = ComCount.objects.filter(post=post, user=user).exists()

    # If a ComCount instance doesn't exist, create and save a new one
    if not com_count_exists:
        # Get the count of existing ComCount instances for the post
        existing_count = ComCount.objects.filter(post=post).count()

        # Create a new ComCount instance for the user and post
        new_com_count = ComCount.objects.create(
            user=user,
            post=post,
            order=existing_count + 1,  # Set the order to the count + 1
        )

    # Get the post and set it for com_count
    
    

    # Save the com_count instance
    

@login_required
def post_like(request, post_id):
  post = Post.objects.get(pk=post_id)
  user = request.user

  if post.like_users.filter(pk=user.pk).exists():
    post.like_users.remove(user)
    
  else:
    #관계 설정
    post.like_users.add(user)
    
  return redirect("board:detail", post_id)


@login_required
def post_scrap (request, post_id):
  post = Post.objects.get(pk=post_id)
  user = request.user

  if post.scrap_users.filter(pk=user.pk).exists():
    post.scrap_users.remove(user)
    
  else:
    post.scrap_users.add(user)
    # Scrap.objects.create(post=post, user=user)
    
  return redirect("board:detail", post_id)


def home(request):
  category_list = Category.objects.all()

  return render(request, "board/home.html", {'category_list': category_list})