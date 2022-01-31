from django.contrib import admin

# Register your models here.
from weblog.models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
