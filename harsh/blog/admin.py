from django.contrib import admin
from .models import Post

class LessonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post)