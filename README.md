# BlogRayiooo
这是一个Django博客。

# 支持库
* django
* pymysql

# 软件工具
PyCharm（IDE）
phpStudy（Apache、MySQL等环境的一键配置工具，超好用！）

# 搭建步骤
* 1.在PyCharm的 File/New Project 中新建一个Django项目。

* 2.在 mysite/settings.py 中修改数据库类型为MySQL，如下：
```python
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

* 3.通过phpStudy的MySQL管理器进入数据库，新建一个数据库'blogdb'，并保持数据库登入账号密码与上面的值相同。

* 4. Django默认帮我们做很多事情，比如User、Session 这些都需要创建表来存储数据，Django已经把这些模块帮我准备好了，我们只需要执行数据库同步，把相关表生成出来即可：
```
mysite> python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
 ```
[摘自cnblogs](https://www.cnblogs.com/fnng/p/3737964.html)

如果在这个过程中出现任何错误，参照 [django数据库错误相关问题](https://blog.csdn.net/pipisorry/article/details/45727309)。

* 5. 要想登录admin后台，必须要有帐号，接下来创建超级管理员帐号。
```
mysite> python manage.py createsuperuser
Username (leave blank to use 'fnngj'): admin    # 管理员帐号
Email address: admin@mail.com      # email
Password:                          # 密码
Password (again):                  # 重复密码
Superuser created successfully.
```
[摘自cnblogs](https://www.cnblogs.com/fnng/p/3737964.html)

# 参考资料