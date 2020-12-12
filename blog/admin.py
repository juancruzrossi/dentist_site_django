from django.contrib import admin
from .models import Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo',)
    resource_class = PostResource
    
admin.site.register(Post, PostAdmin)
