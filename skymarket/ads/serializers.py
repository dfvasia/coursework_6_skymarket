from rest_framework import serializers


from rest_framework.validators import UniqueValidator

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        max_length=128,
        min_length=5,
    )

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=128,
        min_length=10,
        validators=[UniqueValidator(queryset=Ad.objects.all())],
    )

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass
