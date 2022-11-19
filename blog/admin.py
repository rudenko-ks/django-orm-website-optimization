from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'published_at',
    )
    raw_id_fields = (
        'author',
        'likes',
        'tags',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'post',
        'author',
    )
    list_display = (
        'post',
        'author',
        'published_at',
        'text',
    )
