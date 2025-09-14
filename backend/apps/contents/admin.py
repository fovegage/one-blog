from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Tag, Post, Site, CarouselPost, SiteInfo, LinkInfo, SayInfo, RecommendPost, \
    CommonLinkInfo, Introduce

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Site)
admin.site.register(CarouselPost)
admin.site.register(SiteInfo)
admin.site.register(LinkInfo)
admin.site.register(SayInfo)
admin.site.register(Introduce)
admin.site.register(RecommendPost)
admin.site.register(CommonLinkInfo)


# class CategoryAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super(CategoryAdmin, self).get_queryset(request)
#         print(request.user)
#         if request.user.is_superuser:
#             return qs
#         elif request.user == "blog":
#             return qs.filter(type=Category.objects.filter(type=1))
#
#
# admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     print(qs)
    #     if request.user.is_superuser:
    #         return qs
    #     elif request.user == "blog":
    #         return qs.filter(type=Post.objects.filter(type=1))

    list_display = ('title', 'category', 'views', 'create_at', 'is_pass')
    filter_horizontal = ('tag',)
    date_hierarchy = 'create_at'

    list_filter = ['category']
    search_fields = ['title', 'content']
    ordering = ('-create_at',)
    list_per_page = 15
    fields = (
        ('type', 'category', 'nickname', 'is_pass', 'recommend'), 'title', 'tag', 'desc', 'image', 'content',
        'create_at',
        'update_at',
        'url')

    def statusColored(self, obj):
        if obj.is_pass == 0:
            return format_html('<span style="color:red">{}</span>', '审核中')
        else:
            return format_html('<span style="color:green">{}</span>', '已通过')

    statusColored.short_description = "状态"

    # change_form_template = 'record_change_form.html'


admin.site.register(Post, PostAdmin)


class MyAdminSite(admin.AdminSite):
    site_header = '自由之书内容分发系统'
    site_title = '自由之书'


admin_site = MyAdminSite(name='management')
