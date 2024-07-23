from django.urls import path,include

from rest_framework.routers import DefaultRouter

from comment.views import CommentRetrieveUpdateDestroyView, RatingUpdateDeleteView
from post.views import PostModelView



router = DefaultRouter()
router.register('',PostModelView)

urlpatterns = [
    path('post_add/', PostModelView.as_view({'post': 'create'})),
    path('post/', include(router.urls)),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view()),
    path('rating/<int:pk>/', RatingUpdateDeleteView.as_view()),
]