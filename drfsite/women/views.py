# from django.forms import model_to_dict
# from rest_framework import generics, status
# from django.shortcuts import render
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        return Response(WomenSerializer(Women.objects.all(), many=True).data)

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
