from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
  path('signup/', signup_view, name="signup"),
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name="logout"),
  path('mypage/', mypage, name="mypage"),
  path('write_list/', write_list, name='write_list'),
  path('scrap_list/', scrap_list, name='scrap_list'),
]