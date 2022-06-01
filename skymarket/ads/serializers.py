from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from rest_framework.validators import UniqueValidator

from ads.models import Ad


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


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
