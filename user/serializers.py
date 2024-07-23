from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'telegram_chat_id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    telegram = serializers.IntegerField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = [
            'email', 'password', 'password2',
            'username','telegram'
        ]

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password2')
        if pass1 != pass2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs
    
    def create(self, validated_data):
        telegram_chat_id = validated_data.pop('telegram')
        user = User.objects.create_user(**validated_data,telegram_chat_id=telegram_chat_id)
        return user