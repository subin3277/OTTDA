from rest_framework import serializers
from .models import Movie, TV, MovieProvider, TVProvider, SearchMulti


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path')

class TVListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TV
        fields = ('tv_id', 'name', 'poster_path')

class MovieProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieProvider
        fields = '__all__'

class TVProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = TVProvider
        fields = '__all__'

class MultiListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SearchMulti
        fields = ('multi_id', 'title', 'poster_path')

