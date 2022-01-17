from django.db.models.fields import related
from django.urls import path
from django.views.generic.dates import DateDetailView
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    # path('search/', views.Search, name="search"),
    path('about/', views.About, name="about"),
    path('all-articles/', views.AllPosts, name="all-posts"),
    path('article/<int:id>', views.ArticleDetailView, name="article-detail"),
    path('add_post/', views.AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/remove', views.DeletePostView.as_view(), name="delete-post"),
    path('article/<int:pk>/comment', views.AddCommentView.as_view(), name="add-comment"),
    path('article/<int:pk>/<int:id>/sub-comment', views.AddSubCommentView.as_view(), name="add-sub-comment"),
]
