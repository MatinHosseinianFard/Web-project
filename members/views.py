from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, LoginForm
from django.views import View
from weblog.models import Post, Comment
from django.views import View
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(View):

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})


def UserLogout(request):
    logout(request)
    return redirect("home")


@login_required(login_url='login')
def UserProfileView(request, id):
    posts = Post.objects.filter(author=request.user).order_by("-id")
    paginator_1 = Paginator(posts, 3)
    page_number_1 = request.GET.get('page')
    posts = paginator_1.get_page(page_number_1)

    return render(request, "registration/profile.html", {
        "posts": posts,
    })


@login_required(login_url='login')
def PromotePost(request, id):

    post = Post.objects.get(id=id)
    if post.promote:
        post.promote = False
    else:
        post.promote = True
    post.save()

    return HttpResponseRedirect(reverse("profile", args=[request.user.id]))


class CheckCommentView(LoginRequiredMixin, View):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post_id=id)
        return render(request, "registration/check_comment.html", {
            "post": post,
            "post_id": id,
            "comments": comments
        })
        
    def post(self, request, id):
        comment_id = Comment.objects.filter(
            post__id=id).values_list('id', flat=True)
        for c_id in comment_id:
            comment_status = request.POST.get("check%s" % c_id)
            if comment_status and comment_status == "True" or comment_status == "False":
                comment = Comment.objects.get(id=c_id)
                comment.status = comment_status
                comment.save()
            elif comment_status and comment_status == "Delete":
                comment = Comment.objects.filter(id=c_id)
                comment.delete()
        return HttpResponseRedirect(reverse("profile", args=[request.user.id]))
