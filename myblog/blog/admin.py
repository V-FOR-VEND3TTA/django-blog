from django.contrib import admin
from .models import Post

# register the post model to the admin
admin.site.register(Post)
