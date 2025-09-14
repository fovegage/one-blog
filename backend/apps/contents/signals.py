from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Post

# 新建signal文件
# @receiver(pre_save, sender=Post)
# def create_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = instance.create_slug
