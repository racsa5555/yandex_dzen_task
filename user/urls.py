from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView

from user.views import RegistrationView,UserListView

urlpatterns = [
    path('',UserListView.as_view()),
    path('register/',RegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view()),

]