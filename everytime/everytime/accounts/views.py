from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
from board.models import Post

# Create your views here.

def signup_view(request):
  if request.method == "GET":
    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
  
  form = SignUpForm(request.POST)

  if form.is_valid():
    user = form.save()
    return redirect('accounts:login')
  else: return render(request, 'accounts/signup.html', {'form':form})



def login_view(request):
  if request.method == "GET":
    return render(request, 'accounts/login.html', {'form': AuthenticationForm})
  
  form = AuthenticationForm(request, data=request.POST)

  if form.is_valid():
    login(request, form.user_cache)
    return redirect("board:list")
  return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
  return redirect("board:list")

def mypage(request):
  return render(request, 'accounts/mypage.html')


def write_list(request):
  posts = Post.objects.filter(user = request.user)
  return render(request, 'accounts/write_list.html', {'posts': posts})