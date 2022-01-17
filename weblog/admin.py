from django.contrib import admin
from .models import Post, Tag, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)