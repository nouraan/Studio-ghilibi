from django.urls import path

from Movies.views import MoviesListView

app_name = 'movies'

urlpatterns = [
    path('', MoviesListView.as_view(), name='Movies-list'),
]