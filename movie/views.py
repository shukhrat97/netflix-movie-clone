from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Actor, Movie, Comment
from .serializers import MovieSerializers, ActorSerializers, CommentSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# class MovieAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializers = MovieSerializers(movies, many=True)
#         return Response(data=serializers.data)

class HomePageAPIView(APIView):
    def get(self, request):


        return Response({"message": "Home Page! my name is shukhrat"})


# class ActorAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         ser = ActorSerializers(actors, many=True)
#         return Response(data=ser.data)
#     def post(self, request):
#         ser = ActorSerializers(data=request.data)
#         ser.is_valid(raise_exception=True)
#         ser.save()
#         return Response(data=ser.data)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["name"]
    ordering_fields = ["imdb", "-imdb"]
    filterset_fields = ["genre", "year"]

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["actor_id"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actor.add(actor)
        movie.save()
        return Response({"message": "successfully removed"})

    @action(detail=True, methods=['DELETE'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["actor_id"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actor.remove(actor)
        movie.save()
        return Response({"message": "successfully removed"})


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers


class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        serializers = MovieSerializers(movie)
        return Response(data=serializers.data['actor'])


# class CommentAPIView(APIView):
#     def get(self, request):
#         permission_classes = (IsAuthenticated,)
#         authentication_classes = (TokenAuthentication,)
#
#         comments = Comment.objects.filter(user_id=self.request.user)
#         ser = CommentSerializers(comments, many=True)
#         return Response(data=ser.data)

    # def post(self, request):
    #     ser = CommentSerializers(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
    #     return Response(data=ser.data)
    #
    # def delete(self):
    #     pass


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializers

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Comment.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user
        serializer.save()
