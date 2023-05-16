from django.forms import model_to_dict
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        women = Women.objects.all()
        # serializer = WomenSerializer(women, many=True)
        return Response(WomenSerializer(women, many=True).data)

        # lst = Women.objects.all().values()
        # return Response({'post get': list(lst)})


    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(post_new).data})


    # def put(self, request):




# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
