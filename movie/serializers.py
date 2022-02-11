from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movie.models import Movie, Actor, Comment


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthdate(self, value):
        if not str(value) > '1950-01-01':
            raise ValidationError(detail='birthdate should be higher than 01.01.1950')
        return value


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'movie_id',)
