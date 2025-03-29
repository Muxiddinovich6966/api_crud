from rest_framework import serializers

from configapp.models import Movie, Actors


class MovieSerializers (serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

#
# class MovieSerializers (serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=250)
#     slug = serializers.SlugField(read_only=True)
#     year = serializers.IntegerField()
#     actors = serializers.PrimaryKeyRelatedField(many=True,queryset=Actors.objects.all())
#     genre = serializers.CharField()

