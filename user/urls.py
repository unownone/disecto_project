from django.urls import path
from user.views import UserCreate, UserUpdateDelete

urlpatterns = (
    path("user/", UserCreate.as_view()),
    path("user/", UserUpdateDelete.as_view()),
)
