from rest_framework import serializers
from .models import Article, Comment, Recomment


class ArticleListSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class RecommentSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)

    class Meta:
        model = Recomment
        fields = '__all__'
        read_only_fields = ('comment',)

class CommentSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname", read_only=True)

    recomment_set = RecommentSerializer(many=True, read_only=True)
    recomment_count = serializers.IntegerField(source='recomment_set.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source="user.nickname", read_only=True)
    
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



