## 说明

```
## 改造
1. 升级django5
2. 支持一文多发
3. 使用django后台 编辑文章 并发布
4. 迁移整理 书签 现在的pushcode文章
5. AI助手

1. 仅做api 管理由 mweb 进行
2. 主动推送  webhook 推送？  id 使用 commit id (同时保留 id )
3. 如何介入java 网关  feigin?
4. 使用py3Fdfs保存还是oss
5. 仅提供文章功能  用户注册 由java承接
6. 评论gitee和自建  评论由rust承接
7. feed 由 golang 承接
8. 介入jadgger
9. 148服务器数据库备份（备份方案 每天定时备份到nas）
10. 限流由 sential 统一控制
11. gin 承接秒杀模块
```

## todo

```
1. 字段的暴露分层级  暴露到 vo

```

```
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py collectsatices
```

```
null=True
　　数据库中字段可以为空
blank=True
　　django的 Admin 中添加数据时可允许空值
```
