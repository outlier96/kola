from django.contrib import admin

# Register your models here.
from.models import Post, Tag,Subscribers

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Subscribers)