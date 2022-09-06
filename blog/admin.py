from django.contrib import admin
from blog.models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', ]
    search_fields = ['title', ]
    list_per_page = 5

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('post.read'):
            return [f.title for f in self.model._meta.fields]
        return super(PostAdmin, self).get_readonly_fields(
            request, obj=obj
        )
    # pass


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', ]
    search_fields = ['name', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
