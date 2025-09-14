import json

from django.http.response import JsonResponse
from django.shortcuts import HttpResponse
from django.views.generic import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import TagFilter, PostFilter, CategoryFilter, SiteInfoFilter, BlogTypeFilter, SayInfoFilter, \
    IntroduceFilter, RecommendPostFilter
from .models import Site, Post, Tag, Category, CarouselPost, SiteInfo, SayInfo, Introduce, RecommendPost, \
    CommonLinkInfo
from .serializers import PostSerializer, TagSerializer, CategorySerializer, CarouselPostSerializer, SiteInfoSerializer, \
    BlogTypeSerializer, SayInfoSerializer, IntroduceSerializer, RecommendPostSerializer, CommonLinkInfoSerializer


class CommonLinkInfoViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CommonLinkInfoSerializer
    queryset = CommonLinkInfo.objects.all()


class SayInfoViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SayInfoSerializer
    queryset = SayInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = SayInfoFilter


class IntroduceViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = IntroduceSerializer
    queryset = Introduce.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = IntroduceFilter


class RecommendPostViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = RecommendPostSerializer
    queryset = RecommendPost.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = RecommendPostFilter


class BlogTypeViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = BlogTypeSerializer
    # queryset = BlogType.objects.filter(blog_category__category_type=1)
    queryset = Site.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = BlogTypeFilter


class PostPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'per_page'
    page_query_param = 'page'

    # def get_paginated_response(self, data):
    #     ###可选方法，自定义分页的返回结果
    #     ret = {
    #         'count': self.page.paginator.count,
    #         'next': self.get_next_link(),
    #         'previous': self.get_previous_link(),
    #         'data': data
    #     }
    #     return Response(ret)


# CacheResponseMixin 缓存
# RetrieveCacheResponseMixin
class PostViewSet(ListModelMixin, RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    queryset = Post.objects.filter(is_pass=True)
    filter_class = PostFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['create_at', 'update_at', 'views']

    # def get_queryset(self):
    #     blog_type = self.request.GET
    #     if len(blog_type) == 0:
    #         return Post.objects.all()
    #     elif 'type' in blog_type:
    #         return Post.objects.filter(type=blog_type['type'])
    #
    #     elif 'recommend' in blog_type:
    #         return Post.objects.filter(recommend=blog_type['recommend'])
    # if blog_type['recommend'] == 1:
    #     print(blog_type)
    #     return Post.objects.filter(recommend=True)
    # else:
    #     print(blog_type)
    #     return Post.objects.filter(recommend=False)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(category_type=1)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = CategoryFilter
    ordering_fields = ['index']


class TagViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = TagFilter


class CarouselPostViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CarouselPostSerializer
    queryset = CarouselPost.objects.all()


class SiteInfoViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SiteInfoSerializer
    queryset = SiteInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = SiteInfoFilter


class CommonInfo(View):
    def post(self, request):
        return JsonResponse({'a': 1})


def category(request, title):
    qs = Site.objects.get(blog_type=title).category_set.values_list('cname')
    print(qs)
    # print({id:name for id name in (enumerate([cname[0] for cname in qs])) })
    dt = dict(enumerate([cname[0] for cname in qs]))
    ds = [{'id': id, 'name': name} for id, name in dt.items()]
    print(ds)
    result = 1
    return HttpResponse(json.dumps(ds), content_type="application/json")


def tag(request, tag):
    from django.db import connection
    p = Tag.objects.get(id=6).tag_post.all()
    print(p)
    # p = Post.objects.get(id=1).tag
    # print(p)
    print(connection.queries)
    # qs = BlogType.objects.get(blog_type=tag).tag_set.values_list('tname')
    # print(qs)
    # # print({id:name for id name in (enumerate([cname[0] for cname in qs])) })
    # dt = dict(enumerate([cname[0] for cname in qs]))
    # ds = [{'id': id, 'name': name} for id, name in dt.items()]
    # print(ds)
    # result = 1
    return HttpResponse(json.dumps({"name": 1}), content_type="application/json")
