from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Movie, Actors
from .serializers import MovieSerializers, ActorSerializers
from rest_framework.generics import CreateAPIView

class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class ActorCreateView(CreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializers

class MovieViewSet(ViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    @action(detail=True, methods=['post'])
    def actor_add(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        actor = get_object_or_404(Actors, id=actor_id)
        movie.actors.add(actor)
        return Response({"message": "Actor qushildi"}, status=status.HTTP_200_OK)

# class MovieApi(APIView):
#     def get(self,request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies,many=True)
#         return Response(data=serializer.data,status = status.HTTP_200_OK)
#
#     def post(self,request):
#         data = {"qushldi":True}
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             data["serializer"] = serializer.data
#             return Response(data=data)
#         data["qushildi":False]
#         return Response(data=data)
#
#
# class MovieDetailApi(APIView):
#     def get(self,request,slug):
#         response = {"Bajarildi":True}
#         try:
#             movie = Movie.objects.get(slug=slug)
#             serializer = MovieSerializers(movie)
#             response["data"] = serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response["Bajarildi"]=False
#             return Response(data=response)
#
#
#     def put(self,request,slug):
#         response = {"Bajarildi":True}
#         try:
#             movie = Movie.objects.get(slug=slug)
#             serializer = MovieSerializers(movie,data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#             return Response(data=serializer.data)
#         except Movie.DoesNotExist:
#             response["Bajarildi"]=False
#             return Response(data=response)





#
# @api_view(["GET", "POST"])
# def movie_list_create(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializers(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "POST":
#         serializer = MovieSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# def movie_detail(request, slug):
#     movie = get_object_or_404(Movie, slug=slug)
#
#     if request.method == "GET":
#         serializer = MovieSerializers(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method in ["PUT", "PATCH"]:
#         serializer = MovieSerializers(movie, data=request.data, partial=(request.method == "PATCH"))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         movie.delete()
#         return Response({"message": "Movie muvofaqiyatli uchirildi"}, status=status.HTTP_204_NO_CONTENT)
