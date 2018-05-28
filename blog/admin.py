from django.contrib import admin
from blog.models import User, ArticleType, Article


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'type', 'content', 'timestamp']


admin.site.register(User, UserAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
