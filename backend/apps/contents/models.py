from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from mdeditor.fields import MDTextField

# from uuslug import slugify
BLOG_TYPE = (
    (1, "博客站"),
    (2, "考研站"),
    (5, "自由站"),
    (4, "番号站")
)

LINK_TYPE = (
    (1, "左邻右舍"),
    (2, "旗下网站"),
    (3, "工具网站"),
    (4, "优秀博客")
)

CATEGORY_TYPE = (
    (1, '一级分类'),
    (2, '二级分类')
)

C_TYPE = (
    (1, 'category'),  # 分类
    (2, 'page'),  # 单页
    (3, 'custom')  # 自定义
)


class Site(models.Model):
    """
    可创建多个站点
    """
    # 使用自增主键关联 不允许为空
    title = models.CharField(verbose_name="站点", max_length=100)

    class Meta:
        verbose_name = "站点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    """
    分类: 无限极分类
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name="blog_category", verbose_name="站点")
    category_type = models.IntegerField(verbose_name='分类类型', choices=C_TYPE)
    title = models.CharField(verbose_name="分类", max_length=16)
    desc = models.TextField(verbose_name="描述", null=True, blank=True)
    # 1 目录 2 单独page 3 自定义url
    # cate_type = models.SmallIntegerField(verbose_name="分类类型", choices=C_TYPE, null=True, blank=True)
    index = models.SmallIntegerField(verbose_name='目录顺序', default=1)
    url = models.CharField(verbose_name="url", max_length=100, null=True, blank=True)
    icon = models.CharField(verbose_name="icon", max_length=20, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='sub_cat', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name="添加日期", default=datetime.now)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    标签：多对多
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name='blog_tag', verbose_name="站点")
    title = models.CharField(verbose_name="标签", max_length=16)
    description = models.TextField(verbose_name="描述", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name="添加日期", default=datetime.now)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    文章
    """
    statusChoices = (
        (0, '停用'),
        (1, '在用')
    )
    # models.TextChoices 理解 继承dict的意义
    # models.ManyToManyRel
    # 加入 snowid
    type = models.SmallIntegerField(verbose_name="站点", choices=BLOG_TYPE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类",
                                 related_name="category_post")
    # category = models.CharField(verbose_name="分类", max_length=20)
    nickname = models.CharField(verbose_name="作者", max_length=12, default="嘉美伯爵")
    title = models.CharField(verbose_name="标题", max_length=250)
    # slug = models.SlugField(max_length=100)
    # serialize =TextField(verbose_name="描述",serialize=)
    description = models.TextField(verbose_name="描述")
    raw_url = models.URLField(verbose_name="原文地址", null=True, blank=True)
    cover = models.ImageField(verbose_name="封面", null=True, blank=True, upload_to='post/%Y/%m/%d')
    content = MDTextField(verbose_name="文章内容")
    # 浏览量
    views = models.IntegerField(verbose_name="浏览量", default=0)
    # 点赞
    digg_count = models.IntegerField(verbose_name="点赞量", default=0)
    # 分享
    share_count = models.IntegerField(verbose_name="分享量", default=0)
    # 收藏
    collect_count = models.IntegerField(verbose_name="收藏量", default=0)
    create_at = models.DateTimeField(verbose_name="发布时间", default=datetime.now)
    update_at = models.DateTimeField(verbose_name="更新时间", default=datetime.now)
    # 不过审邮件通知，用户中心获取，必须登录
    is_pass = models.BooleanField(verbose_name="是否过审")
    # 点赞、浏览量用redis  因为涉及浏览修改
    # 教程 直接给其链接 机器学习
    recommend = models.BooleanField(verbose_name="是否推荐", default=False)
    # 该文章是否启用评论
    comment_status = models.BooleanField(verbose_name="评论状态", default=True)
    tag = models.ManyToManyField(Tag, verbose_name="文章标签", related_name="tag_post")
    status = models.IntegerField(choices=statusChoices, verbose_name='状态', default=1)

    # 评论外键（分布式事务？）

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('create_at',)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def create_slug(self):
        slug = slugify(self.title)
        qs = self.objects.filter(slug=slug)
        if qs:
            new_slug = f'{slug}-{qs.count()}'
            return new_slug

        return slug


# from django.contrib.auth import get_user_model

class SiteInfo(models.Model):
    """
    站点信息
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, verbose_name="站点")
    tip = models.CharField(verbose_name="top栏", max_length=50)
    # logo = models.ImageField(verbose_name="logo")
    copyright = models.CharField(verbose_name="版权", max_length=100)
    title = models.CharField(verbose_name="网站名称", max_length=20)
    site_description = models.CharField(verbose_name="网站描述", max_length=100, blank=True, null=True)
    html_description = models.CharField(verbose_name="desc", max_length=100, blank=True, null=True)
    ad_image = models.ImageField(verbose_name="引流", blank=True, null=True)
    notice = models.TextField(verbose_name="公众内容")
    # 前端 /about 写死
    about = RichTextField(verbose_name="关于", blank=True, null=True)
    avatar = models.ImageField(verbose_name="头像")
    wechat = models.ImageField(verbose_name="公众号")
    keywords = models.CharField(verbose_name="key", max_length=100, blank=True, null=True)

    # 一次性发布验证
    # verify_name = models.CharField(verbose_name="name", max_length=100, null=True, blank=True)
    # verify_content = models.CharField(verbose_name="content", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tip


class CarouselPost(models.Model):
    """
    广告/文章（轮播）
    """
    # post = models.OneToOneField(to=Post, verbose_name='所属文章', on_delete=models.CASCADE, null=True, blank=True)
    site = models.ForeignKey(to=SiteInfo, verbose_name='站点广告', on_delete=models.CASCADE, related_name="carousel",
                             null=True, blank=True)
    image = models.ImageField(verbose_name='轮播图(800*200)广告(360*120)', upload_to='carouse/%Y/%m/%d')
    url = models.URLField(verbose_name="图片网址", blank=True, null=True)
    index = models.IntegerField(default=1, verbose_name='轮播顺序')
    # 0:自有 1:广告 2:方图
    type = models.SmallIntegerField(verbose_name="图片类型", default=0)
    title = models.CharField(verbose_name="desc", max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.site)


class LinkInfo(models.Model):
    """
    友链：优秀的学习笔记
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name='blog_link', verbose_name="站点")
    name = models.CharField(verbose_name="网站标题", max_length=50)
    desc = models.TextField(verbose_name="网站描述", null=True, blank=True)
    url = models.URLField(verbose_name="网站链接")

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)


class SayInfo(models.Model):
    """
    说说/公告
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, verbose_name="站点")
    content = models.CharField(max_length=200, verbose_name="说说内容")
    # link = models.URLField(verbose_name="说说链接", null=True, blank=True)
    add_date = models.DateTimeField(verbose_name="说说日期", default=datetime.now)

    class Meta:
        verbose_name = '说说'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Introduce(models.Model):
    """
    网站介绍页面
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name='blog_introduce', verbose_name="站点")
    title = models.CharField(max_length=60, verbose_name="标题")
    content = RichTextField(verbose_name="内容")
    update_date = models.DateTimeField(verbose_name="更新日期", default=datetime.now)

    class Meta:
        verbose_name = '介绍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.type)


class RecommendPost(models.Model):
    """
    推荐: redis同步
    """
    type = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name='recommend_introduce',
                             verbose_name="站点")
    # 文章id
    url = models.SmallIntegerField(unique=True)
    # 与该文章匹配的文章，机器学习做 存json
    link_post = models.TextField(verbose_name="推荐")

    class Meta:
        verbose_name = '推荐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.type)


class CommonLinkInfo(models.Model):
    """
    公共友链
    """
    type = models.SmallIntegerField(choices=LINK_TYPE, verbose_name="友链类型")
    name = models.CharField(verbose_name="网站标题", max_length=100)
    desc = models.TextField(verbose_name="网站描述", null=True, blank=True)
    url = models.URLField(verbose_name="网站链接")
    avatar = models.URLField(verbose_name="avatar", null=True, blank=True)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
