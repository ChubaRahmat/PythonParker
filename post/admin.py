from django.contrib import admin

# Register your models here.
# Здесь регистируруются модели для их отображения в админ панели
from post.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)