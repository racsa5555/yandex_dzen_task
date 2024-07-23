from django.contrib import admin
from comment.models import Comment,Rating

admin.site.register(Comment)
admin.site.register(Rating)