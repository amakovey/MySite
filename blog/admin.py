from django.utils import timezone
from django.contrib import admin
from .models import Post, Comments


def make_published_now(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())


make_published_now.short_description = "Publish now"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author' , 'text', 'created_date', 'published_date')
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('Text', {'fields': ['text']}),
        ('Created date', {'fields': ['created_date']}),
        ('Published date', {'fields': ['published_date']}),
    ]

    actions = [make_published_now]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'created_date')
    fieldsets = [
        ('Автор', {'fields': ['author']}),
        ('Title', {'fields': ['title']}),
        ('Text', {'fields': ['text']}),
        ('Created date', {'fields': ['created_date']}),
    ]
    list_filter = ['title']
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
