class DBRouter(object):
    """数据库配置"""

    def db_for_read(self, model, **hints):
        return 'default'
        # import random
        # return random.choice(['slave1', 'slave2'])

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True
