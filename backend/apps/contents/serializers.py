from rest_framework import serializers
from .models import Post, Category, Tag, CarouselPost, SiteInfo, Site, SayInfo, Introduce, LinkInfo, RecommendPost, \
    CommonLinkInfo


class LinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkInfo
        fields = "__all__"


class CommonLinkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonLinkInfo
        fields = "__all__"


class RecommendPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendPost
        fields = "__all__"


class IntroduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduce
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(read_only=True)

    def get_count(self, obj):
        return Post.objects.filter(tag__tname=obj).count()

    class Meta:
        model = Tag
        fields = "__all__"


class ShowPostSerializer(serializers.ModelSerializer):
    # 只获取文章信息
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Post
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    # category_post = ShowPostSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class BlogTypeSerializer(serializers.ModelSerializer):
    blog_category = CategorySerializer(many=True)
    blog_tag = TagSerializer(many=True)
    blog_link = LinkInfoSerializer(many=True)
    blog_introduce = IntroduceSerializer(many=True)
    blog_info = serializers.SerializerMethodField(read_only=True)
    recommend_introduce = RecommendPostSerializer(many=True)

    def get_blog_info(self, obj):
        btype = obj.blog_type
        tag_count = Tag.objects.filter(type__blog_type=btype).count()
        category_count = Category.objects.filter(type__blog_type=btype).count()
        last_essay = str(Post.objects.filter(type=btype).last().create_at)[:10]
        essay_count = Post.objects.filter(type=btype).count()
        comments = 0
        return {'tcount': tag_count, 'ccount': category_count, 'last_essay': last_essay, 'pcount': essay_count,
                'comments': comments}

    class Meta:
        model = Site
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer()
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    pre_link = serializers.SerializerMethodField(read_only=True)
    next_link = serializers.SerializerMethodField(read_only=True)

    def get_pre_link(self, obj):
        # print(list(self._args)[0][obj])
        first = Post.objects.first()
        if obj.id == 1:
            return None
        return obj.id - 1

    def get_next_link(self, obj):
        last_id = Post.objects.last().id
        if obj.id == last_id:
            return None

        return obj.id + 1

    class Meta:
        model = Post
        fields = "__all__"


class CarouselPostSerializer(serializers.ModelSerializer):
    # site = SiteInfoSerializer()

    class Meta:
        model = CarouselPost
        fields = "__all__"


class SiteInfoSerializer(serializers.ModelSerializer):
    carousel = CarouselPostSerializer(many=True)

    def get_attribute(self, instance):
        print(instance)

    class Meta:
        model = SiteInfo
        fields = "__all__"


class SayInfoSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SayInfo
        fields = "__all__"
