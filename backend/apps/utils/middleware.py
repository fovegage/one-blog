#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：blog-api
@File    ：middleware.py
@Author  ：fovegage
@Email   ：fovegage@gmail.com
@Date    ：10/8/22 10:30 PM
"""

import nacos
from django.utils.deprecation import MiddlewareMixin


class RegisterNacos(MiddlewareMixin):
    metadata = {
        "preserved.register.source": "SPRING_CLOUD",
    }
    SERVER_ADDRESSES = "192.168.12.126:8848"
    NAMESPACE = "public"
    try:
        # auth mode
        client = nacos.NacosClient(
            server_addresses=SERVER_ADDRESSES,
            namespace=NAMESPACE,
            username="nacos",
            password="nacos"
        )
        resp = client.add_naming_instance(
            service_name="blog-api",
            ip="192.168.12.56",
            port="8000",
            cluster_name='DEFAULT',
            group_name='DEFAULT_GROUP',
            metadata=metadata,
            ephemeral=False  # 临时实例
        )
        print("注册成功")
    except:
        print("注册失败")
