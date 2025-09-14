"""blogapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, re_path
from apps.contents.views import category, tag
from apps.contents.views import PostViewSet, TagViewSet, CategoryViewSet, CarouselPostViewSet, SiteInfoViewSet, \
    BlogTypeViewSet, SayInfoViewSet, IntroduceViewSet, CommonInfo, RecommendPostViewSet, CommonLinkInfoViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from blogapi.settings import MEDIA_ROOT

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register(r'siteinfo', SiteInfoViewSet)
router.register(r'blog', BlogTypeViewSet)
router.register(r'say', SayInfoViewSet)
router.register(r'introduce', IntroduceViewSet)
router.register(r'recommend', RecommendPostViewSet)
router.register(r'link', CommonLinkInfoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'docs/', include_docs_urls(title='嘉美伯爵')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^test/(?P<obj_id>\d+)', hello),
    # url(r'^test/(\S+)/', hello),
    url(r'^category/(?P<title>.+)/$', category),
    url(r'^tag/(?P<tag>.+)/$', tag),
    url(r'^common/', CommonInfo.as_view()),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # api
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
