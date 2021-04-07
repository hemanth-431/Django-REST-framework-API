from django.contrib import admin
from django.urls import path,include
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from core.views import PostView,PostCreateView,TestView,PostListCreateView,loginPage,registerPage,home,Postregister
from django.conf.urls import url
from Tools.scripts import serve
from drf_api import settings

urlpatterns = [
     path('rest-auth/', include('rest_auth.urls')),
     path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('postview/',PostView.as_view(),name='test'),
    path('postreg/',Postregister.as_view(),name='reg'),
    path('create/',PostCreateView.as_view(),name='create'),
    path('test/',TestView.as_view(),name='create'),
    path('list-create/',PostCreateView.as_view(),name='list-create'),
     path('hemanth/',PostListCreateView.as_view(),name='list'),
    path('api/token/',obtain_auth_token,name='obtain-token'),
    path('login/',loginPage,name='login'),
    path('',registerPage),
    path('home/',home),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
