from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from comment.models import Comment, Rating

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author_name','text']

class RatingSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    mark_number = serializers.IntegerField()


    class Meta:
        model = Rating
        fields = ['mark_number','author']

    def validate_mark_number(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError('Рейтинг должен быть между 1 и 5')
        return value
    
    def create(self, validated_data):
        rate = validated_data.pop('mark_number')
        rating = Rating.objects.create(**validated_data,rating = rate)
        return rating
