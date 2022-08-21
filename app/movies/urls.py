from django.urls import path, include

from .views import MovieViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

# movie_list = MovieViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# movie_detail = MovieViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     path("api/movies/", MovieList.as_view()),
#     path("api/movies/<int:pk>/", MovieDetail.as_view()),
# ]

# urlpatterns = [
#     path("api/movies/", movie_list, name='movie-list'),
#     path("api/movies/<int:pk>/", movie_detail, name='movie-detail'),
# ]

urlpatterns = [
    path('', include(router.urls)),
]