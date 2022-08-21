from django.urls import path

from .views import MovieList, MovieDetail, MovieViewSet

movie_list = MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

movie_detail = MovieViewSet.as_view({
    'get': 'retrieve'
})

# urlpatterns = [
#     path("api/movies/", MovieList.as_view()),
#     path("api/movies/<int:pk>/", MovieDetail.as_view()),
# ]

urlpatterns = [
    path("api/movies/", movie_list, name='movie-list'),
    path("api/movies/<int:pk>/", movie_detail, name='movie-detail'),
]