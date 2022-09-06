from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register(BlogComment)    #tupple for multiple models like--> ((Post,BlogComment))


@admin.register(Post)       #means, register karne ke sath sath admin ko vi change kar rahe hai. injected javaScript in Post admin

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)