import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *

from rest_framework import serializers


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance.update(**validated_data)
#---------------------------------------------------------------------------------------------
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

#
# def encode():
#     model = WomenModel('Angilina','content: Angilina')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angilina","content":"content: Angilina"}')
#     data = JSONParser().parse(stream)
#     serializer =WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
    # class Meta:
    #     model = Women
    #     fields = '__all__'

