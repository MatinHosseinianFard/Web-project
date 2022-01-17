from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogout, name="logout"),
    path('profile/<int:id>', views.UserProfileView, name="profile"),
    path('profile/<int:id>/check-comment', views.CheckCommentView.as_view(), name="check-comment"),
    path('profile/promote/<int:id>', views.PromotePost, name="promote-post"),
]
