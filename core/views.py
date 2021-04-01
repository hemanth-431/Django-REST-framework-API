from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated  ###
from rest_framework.views import APIView  ##generics.py
from rest_framework import generics
from .serializers import PostSerializer,PostReg
from .models import Post,Contact
from core.models import Contact


def registerPage(request):
    # if request.method=="POST":
    #     print('This is post')
    context={}
    return render(request,'register.html',context)
def loginPage(request):
    context={}
    return render(request,'login.html',context)
def home(request):
    if request.method=="POST":
        print('This is post')
        email=request.POST['email']
        name=request.POST['name']
        number=request.POST['number']
        # print(email,name,number)
        ins=Contact(name=name,email=email,number=number)
        ins.save()
        print("data is returned to DB")
    context={}
    return render(request,'home.html',context)

class TestView(APIView):

    # permission_classes=(IsAuthenticated,)  ###

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

class Postregister(APIView):
    def get(self,request,*args,**kwargs):
        qs=Contact.objects.all()
        serializer=PostReg(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=PostReg(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class PostView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset=Post.objects.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    


    

class PostCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()

    def get(self,request,*args,**kwargs):
        qs=Post.objects.all()
        po=qs.first()
        serializer=PostSerializer(po)
        return Response(serializer.data)
        # return self.list(request,*args,**kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class=PostSerializer
    queryset=Post.objects.all()


    

# class TestView(APIView):

#     permission_classes=(IsAuthenticated,)  ###

#     def get(self,request,*args,**kwargs):
#         qs=Post.objects.all()
#         # po=qs.first()
#         # serializer=PostSerializer(po)
#         serializer=PostSerializer(qs,many=True)
#         # data={
#         #     'name':'john',
#         #     'age':23
#         # }
#         return Response(serializer.data)

#     def post(self,request,*args,**kwargs):
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)



# def test_view(request):
#     data={
#         'name':'john',
#         'age':23

#     }
#     return JsonResponse(data)
