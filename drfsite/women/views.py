from django.forms import model_to_dict
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import WomenSerializer

# gent & post
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


#
# class WomenAPIView(APIView):
#     def get(self, request):
#         return Response(WomenSerializer(Women.objects.all(), many=True).data)
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not alowed, status=status.HTTP_405'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Women not found'})
#
#         serializer = WomenSerializer(instance=instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'put': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not alowed, status=status.HTTP_405'})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': f'Women not found (запись {pk} не найдена:  проверте правильность запроса)'})
#
#         instance.delete()
#         return Response({'delete': f'Women deleted    pk: {str(pk)} {instance}'})
