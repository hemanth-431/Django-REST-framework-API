from rest_framework import serializers
from .models import Post,Contact
from django import forms
# class PostForm(forms.ModelForm):
#     class Meta:
#         model=Post
#         fields=(
#             'title','description'
#         )
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=(
            'title','description','owner'
        )
class PostReg(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=(
            'email','name','number'
        )