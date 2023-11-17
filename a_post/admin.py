from django.contrib import admin
from .models import *
admin.site.register(Post)
admin.site.register(Tag)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'parent_post', 'body', 'id']
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['author','parent_comment','body','created']
admin.site.register(LikedPost)
admin.site.register(LikedComments)
admin.site.register(Routes)
admin.site.register(Image)