from django.urls import path
from . import views

app_name='board'


urlpatterns = [
  path('', views.list, name="list"),
  path('<int:id>/', views.detail, name="detail"),
  path('create/', views.create, name="create"),
  path('update/<int:id>/', views.update, name="update"),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('<int:id>/comment_create/', views.com_create, name="com_create"),
  path('<int:post_id>/comment_delete/<int:com_id>/', views.com_delete, name="com_delete"),
  path('<int:post_id>/like', views.post_like, name="post_like"),

]