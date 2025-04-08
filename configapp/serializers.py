from rest_framework import serializers

from configapp.models import Movie, Actors, CommitMovie


# class MovieSerializers (serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'
# #

class MovieSerializers (serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(max_length=200)
        slug = serializers.SlugField(read_only=True)
        year = serializers.IntegerField()
        actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actors.objects.all())
        genre = serializers.CharField()

        def create(self, validated_data):
            actors_data = validated_data.pop('actors')
            movie = Movie.objects.create(**validated_data)
            movie.actors.set(actors_data)
            return movie

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.year = validated_data.get('year', instance.year)
            instance.genre = validated_data.get('genre', instance.genre)

            if 'actors' in validated_data:
                actors_data = validated_data.pop('actors')
                instance.actors.set(actors_data)

            instance.save()
            return instance

class ActorSerializers (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    birth_date = serializers.DateField()
    name = serializers.CharField(max_length=100)


    def create(self,validated_data):
        actors = Actors.objects.create(**validated_data)
        return actors

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.birth_date = validated_data.get('birth_date',instance.birth_date)
        instance.save()
        return instance


# class CommitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CommitMovie
#         fields = "__all__"

class CommitSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = CommitMovie
        fields = '__all__'
