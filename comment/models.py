from django.db import models
from django.contrib.auth import get_user_model

from post.models import Post

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=255)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    
class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.rating} => {self.post}'