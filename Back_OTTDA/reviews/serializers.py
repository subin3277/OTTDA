from rest_framework import serializers
from .models import Review, Comment, Recomment


class ReviewListSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'created_at', 'updated_at', 'movie_id')

class RecommentSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)
    class Meta:
        model = Recomment
        fields = '__all__'
        read_only_fields = ('comment',)

class CommentSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)
    recomments = RecommentSerializer(many=True, read_only=True)
    recomment_count = serializers.IntegerField(source='recomments.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source="user.nickname", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'



