from rest_framework import serializers

from .models import *



class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    # class Meta:
    #     model = Women
    #     fields = '__all__'

