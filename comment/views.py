from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework import permissions

from comment.models import Comment, Rating
from comment.serializers import CommentSerializer, RatingSerializer
from post.permissions import IsAuthor, IsStaff


class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsStaff()]
        return [permissions.AllowAny()]


class RatingUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsAuthor()]
        return [permissions.AllowAny()]