from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from comment.models import Comment
from comment.serializers import CommentSerializer, RatingSerializer
from post.models import Post
from post.serializers import PostSerializer
from post.permissions import IsAuthor, IsAuthorOrStaff,IsStaff
from post.utils import send_telegram_message

class PostModelView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        send_telegram_message(post.author.telegram_chat_id, f'Ваш пост успешно опубликован: {post.text}')
   

   
    def get_permissions(self):
        if self.request.method in ('PATCH', 'PUT', 'DELETE'):
            return [IsAuthorOrStaff()]
        return [permissions.AllowAny()]
    

    @action(detail=True, methods=['POST'])
    def comment_add(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response('Успешно добавлено', 201)

    @action(detail=True, methods=['GET'])
    def comment(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, 200)

    @action(detail=True, methods=['POST'])
    def mark_add(self, request, pk=None):
        post = self.get_object()
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post,user=request.user)
        return Response('Успешно добавлено', 201)

        


