from django.http.request import QueryDict
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from Studio_Ghibli.settings import CACHE_TTL
from Movies.api import StudioGhibliApi as api
from . serializer import MyMoviesSerilazier
from rest_framework.response import Response
from rest_framework import views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class MoviesListView(views.APIView):
    def get(self, request):
        #Take Parameters From the URL
        FilmName = self.request.query_params.get('film')
        PersonName = self.request.query_params.get('name')
        Movies=api.Get_Films_And_People()   
        if FilmName != None:
            Film_Filtered_Data=api.Films_Filter(Movies,FilmName)
            results = MyMoviesSerilazier(Film_Filtered_Data, many=True).data
        elif PersonName !=None:
            Person_Filter=api.People_Filtered_Query(PersonName)
            # print('Person_Filter',Person_Filter)
            People_Filtered_Data=api.Get_Films_And_People_Filtered(PersonName)
            results = MyMoviesSerilazier(People_Filtered_Data, many=True).data
        else:
            results = MyMoviesSerilazier(Movies, many=True).data
      
        return Response(results)

# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
# class MoviesListView(generics.ListAPIView):
#     def get_queryset(self):
#         queryset =api.Get_Films_And_People()
#         serializer_class = MyMoviesSerilazier
#         return queryset