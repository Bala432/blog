from django.urls import path
from .views import BlogDetailView, UserBlogListView, BlogsCreateView, BlogsListView

urlpatterns = [
    path('user/<str:pk>',UserBlogListView.as_view()),
    path('list',BlogsListView.as_view()),
    path('list/<int:pk>', BlogDetailView.as_view()),
    path('users/create',BlogsCreateView.as_view()),
    #  path('create-user',UserCreateView.as_view()),
]