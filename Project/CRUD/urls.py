from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/create/', views.create_movie, name='create_movie'),
    path('movie/<int:pk>/update/', views.update_movie, name='update_movie'),
    path('movie/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]