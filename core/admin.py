from django.contrib import admin
from core.models import Contact
from .models import Post
admin.site.register(Post)
admin.site.register(Contact)
