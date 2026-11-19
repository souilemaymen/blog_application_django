
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'slug',
        'author',
        'publish',
        'status'
    ]

    list_filter = [
        'status',
        'created',
        'author',
        'publish'
    ]

    search_fields = [
        'title',
        'body',
        'author__username',
        'author__first_name',
        'author__last_name'
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }

    raw_id_fields = [
        'author'
    ]

    date_hierarchy = 'publish'

    ordering = [
        'status',
        'publish'
    ]

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user

        super().save_model(request, obj, form, change)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'post',
        'created',
        'active'
    ]

    list_filter = [
        'active',
        'created',
        'updated'
    ]

    search_fields = [
        'name',
        'email',
        'body'
    ]
