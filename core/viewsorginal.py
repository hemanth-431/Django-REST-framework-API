from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  ###
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class TestView(APIView):

    permission_classes=(IsAuthenticated,)  ###

    def get(self,request,*args,**kwargs):
        qs=Post.objects.all()
        # po=qs.first()
        # serializer=PostSerializer(po)
        serializer=PostSerializer(qs,many=True)
        # data={
        #     'name':'john',
        #     'age':23
        # }
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# def test_view(request):
#     data={
#         'name':'john',
#         'age':23

#     }
#     return JsonResponse(data)
