from django.contrib import admin
from .models import Post, Category, Tag, Like, Bookmark, Project


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    ...


admin.site.register(Tag, TagAdmin)



class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'updated', 'views', 'published']
    list_display_links = ['id', 'title']
    list_filter = ['author', 'created', 'updated', 'published']
    search_fields = ['title', 'content']
    date_hierarchy = 'created'
    ordering = ['-created']
    list_editable = ['published']


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created')


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created')


admin.site.register(Bookmark, BookmarkAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created')


admin.site.register(Like, LikeAdmin)
