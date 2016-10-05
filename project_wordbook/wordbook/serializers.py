from rest_framework import serializers
from wordbook.models import Word
import os
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

# class WordSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Word
        # fields = ('pk', 'created', 'word', 'mean', 'example', 'image')

class WordSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    word = serializers.CharField(required=True, max_length=100)
    mean = serializers.CharField(max_length=100)
    # example은 model에서 TextField()로 정의되어 있지만,
    # serializers는 TextField()를 지원하지 않으므로 CharField()로 변경
    example = serializers.CharField()
    image = serializers.ImageField(write_only=True)

    image_url = serializers.SerializerMethodField('get_image', read_only=True)
    image_thumb_url = serializers.SerializerMethodField('get_thumb', read_only=True)

    def get_thumb(self, obj):
        # 100x100의 size 으로 thumbail 가져오기
        thumbUrl = get_thumbnail(obj.image, '100x100', crop='center', quality=99).url
        return settings.IMAGE_SERVER_URL + thumbUrl

    def get_image(self, obj):
        imageUrl = obj.image.url
        return settings.IMAGE_SERVER_URL + imageUrl

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.image != validated_data.get('image', instance.image):
            # 기존 image과 현재 image이 다르면 파일경로에서 기존 image 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.path))
            # cached db에 있는 thumbnail도 제거
            delete(instance.image)

        instance.word = validated_data.get('word', instance.word)
        instance.mean = validated_data.get('mean', instance.mean)
        instance.example = validated_data.get('example', instance.example)
        instance.save()
        return instance
