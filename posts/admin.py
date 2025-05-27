from django.contrib import admin
from .models import Posts


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'is_published', 'created_at', 'author']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    exclude = ['author']
    view_on_site = False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # superuser sees all posts
        return qs.filter(author=request.user)  # normal admin sees only their posts

    # def has_change_permission(self, request, obj=None):
    #     if obj is None or request.user.is_superuser:
    #         return True
    #     return obj.author == request.user  # can only edit own posts

    # def has_delete_permission(self, request, obj=None):
    #     if obj is None or request.user.is_superuser:
    #         return True
    #     return obj.author == request.user  # can only delete own posts




admin.site.register(Posts, PostAdmin)