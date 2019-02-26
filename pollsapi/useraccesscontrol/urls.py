from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .apiview import UserCreate, UserList, UserRetrieve, LoginView


urlpatterns = format_suffix_patterns([
    path('users/', UserCreate.as_view(), name=UserCreate.name),
    path('users-list/', UserList.as_view(), name=UserList.name),
    path('users-list/<int:pk>/', UserRetrieve.as_view(), name=UserRetrieve.name),
    path('login/', LoginView.as_view(), name=LoginView.name),
])
