import django_filters
from .models import Post, Site, Tag, Category, SiteInfo, SayInfo, Introduce, RecommendPost


class PostFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Post
        fields = ['recommend', 'type', 'category__title', 'tag__title']


class SiteInfoFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SiteInfo
        fields = ['type']


class BlogTypeFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Site
        fields = ['id']


class CategoryFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Category
        fields = ['type']


class TagFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Tag
        fields = ['type']


class SayInfoFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SayInfo
        fields = ['type']


class IntroduceFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Introduce
        fields = ['type']


class RecommendPostFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = RecommendPost
        fields = ['url']
