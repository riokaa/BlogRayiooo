from django.contrib import admin
from blog.models import User, ArticleType, Article


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'type', 'content', 'timestamp', 'click']


admin.site.register(User, UserAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
