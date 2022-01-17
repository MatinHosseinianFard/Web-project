from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db.models import Q
from django.db.models import Count
from itertools import chain
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def Home(request):

    posts = Post.objects.all().order_by('-id')[:3]

    paginator_2 = Paginator(Post.objects.all().order_by("-visitors"), 2)
    page_number_2 = request.GET.get('page2')
    most_view = paginator_2.get_page(page_number_2)

    paginator_3 = Paginator(Post.objects.all().annotate(
        num_comments=Count('comments')).order_by('-num_comments'), 2)
    page_number_3 = request.GET.get('page3')
    most_comment = paginator_3.get_page(page_number_3)

    last_six_slider = Post.objects.filter(promote=True)[:6]
    remaining_slider = Post.objects.exclude(id__in=[ z.id for z in list(last_six_slider) ]).order_by("-visitors")[:6-last_six_slider.count()]

    slider = list(chain(last_six_slider, remaining_slider))

    return render(request, "weblog/index.html", {
        "posts": posts,
        "most_view": most_view,
        "most_comment": most_comment,
        "slider": slider,
    })


def AllPosts(request):
    query = ValueIsValid(request.GET.get('q'))
    date_min = ValueIsValid(request.GET.get('d_min'))
    date_max = ValueIsValid(request.GET.get('d_max'))
    order_by_date = ValueIsValid(request.GET.get('o_date'))
    order_by_view = ValueIsValid(request.GET.get('o_view'))
    resault = Post.objects.all().order_by("-id")

    if query:
        resault = resault.filter(Q(title__icontains=query) | Q(
            body__icontains=query) | Q(category__name__icontains=query))

    if order_by_date:
        resault = resault.order_by(order_by_date)

    if order_by_view:
        resault = resault.order_by(order_by_view)

    if date_min and date_max:
        resault = resault.filter(date__gte=date_min)
        resault = resault.filter(date__lte=date_max)
        resault = resault.order_by("-id")

    paginator_1 = Paginator(resault, 3)
    page_number_1 = request.GET.get('page1')
    posts = paginator_1.get_page(page_number_1)

    paginator_2 = Paginator(Post.objects.all().order_by("-visitors"), 2)
    page_number_2 = request.GET.get('page2')
    most_view = paginator_2.get_page(page_number_2)

    paginator_3 = Paginator(Post.objects.all().annotate(
        num_comments=Count('comments')).order_by('-num_comments'), 2)
    page_number_3 = request.GET.get('page3')
    most_comment = paginator_3.get_page(page_number_3)

    return render(request, "weblog/posts_page.html", {
        "posts": posts,
        "most_view": most_view,
        "most_comment": most_comment,
        "query": query,
        "o_date": order_by_date,
        "o_view": order_by_view,
        "d_min": date_min,
        "d_max": date_max
    })


def ArticleDetailView(request, id):

    post = get_object_or_404(Post, id=id)
    post.visitors += 1
    post.save()

    comments = Comment.objects.filter(parent__isnull=True, post=post,status=True)

    return render(request, "weblog/article_details.html", {
        "post": post,
        "comments": comments,
    })


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = 'login'
    template_name = "weblog/add_post.html"


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    login_url = 'login'
    template_name = "weblog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super(AddCommentView, self).form_valid(form)



class AddSubCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    login_url = 'login'
    template_name = "weblog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        comment = Comment.objects.get(id=self.kwargs["id"])
        form.instance.parent = comment
        comment.child.add(form.save())
        comment.save()
        return super(AddSubCommentView, self).form_valid(form)



class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditForm
    login_url = 'login'
    template_name = "weblog/update_post.html"

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        else:
            return False



class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    login_url = 'login'
    template_name = "weblog/delete_post.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        else:
            return False


def About(request):
    return render(request, "weblog/about.html")


def ValueIsValid(value):
    resault = value != "" and value is not None
    if resault:
        return value
    return resault
