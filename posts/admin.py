from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'likes']
    list_display_links = ['title']
    list_editable = ['image', 'likes']
    search_fields = ['created_at']
    list_filter = ['created_at']