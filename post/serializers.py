from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings:
            return sum(r.rating for r in ratings) / len(ratings)
        return 0
