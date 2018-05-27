# BlogRayiooo
这是一个Django博客。

[更方便地查看文档](https://www.zybuluo.com/rayiooo/note/1155365)

|Author|爱吃大板|
|---|---|
|Email|rayiooo@foxmail.com|

# 1 支持python库（python3.6）
* django
* pymysql
* mod_wsgi

# 2 软件工具
* PyCharm（IDE）
* phpStudy（Apache2.4/32位、MySQL等环境的一键配置工具，超好用！）

# 3 搭建步骤
## 3.1 准备工作
### 3.1.1 新建项目
在PyCharm的`File/New Project`中新建一个Django项目。

### 3.1.2 修改数据库类型
在`mysite/settings.py`中修改数据库类型为MySQL，如下：

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

### 3.1.3 创建数据库
通过phpStudy的MySQL管理器进入数据库，新建一个数据库`blogdb`，并保持数据库登入账号密码与上面的值相同。

### 3.1.4 执行数据库同步
Django默认帮我们做很多事情，比如User、Session 这些都需要创建表来存储数据，Django已经把这些模块帮我准备好了，我们只需要执行数据库同步，把相关表生成出来即可：[↻](https://www.cnblogs.com/fnng/p/3737964.html)

```text
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

如果在这个过程中出现任何错误，参照 [django数据库错误相关问题](https://blog.csdn.net/pipisorry/article/details/45727309)。

### 3.1.5 创建超管账号
要想登录admin后台，必须要有帐号，接下来创建超级管理员帐号。[↻](https://www.cnblogs.com/fnng/p/3737964.html)

```text
mysite> python manage.py createsuperuser
Username (leave blank to use 'fnngj'): admin    # 管理员帐号
Email address: admin@mail.com      # email
Password:                          # 密码
Password (again):                  # 重复密码
Superuser created successfully.
```

### 3.1.6 运行本地服务器
在PyCharm中直接运行程序，服务器即可启动。当然也可以通过`python manage.py runserver`命令行指令执行。

访问 [127.0.0.1:8000](http://127.0.0.1:8000) 以及 [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 即可在本地查看主界面和admin界面。

![login.png](https://i.loli.net/2018/05/27/5b0a6f4165515.png)

## 3.2 部署服务器端
特别参考：[windows 下 apache 部署 django python3.6](https://blog.csdn.net/u012846792/article/details/77712958)

**特别强调注意**的是：apache 的位制和python的位制必须一致（即apache 32位的就只能安装python 32位的，64位也一样）网上很多教程没强调这一点，导致后续的很多工作白费，还找不到问题所在！

因此如果使用phpStudy的apache 32位，就必须使用python 32位。

### 3.2.1 mod_wsgi安装
通过`pip install mod_wsgi`安装mod_wsgi。

如果无法直接安装，就到[https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi)下载whl文件，放到任意目录下，并在该目录下启动cmd，输入`pip install 文件名.whl`安装模块。

比如Apache2.4、python3.6/32位就选择下载`mod_wsgi‑4.6.4+ap24vc14‑cp36‑cp36m‑win32.whl`。

### 3.2.2 部署wsgi模块到apache
在命令行中输入以下指令：
```
mod_wsgi-express module-config
```

可以看到以下wsgi模块位置的输出结果，将它们复制下来。（在cmd中选中、右击即可复制粘贴。）
>LoadFile "c:/program files (x86)/python36/python36.dll"
>
>LoadModule wsgi_module "c:/program files (x86)/python36/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win32.pyd"
>
>WSGIPythonHome "c:/program files (x86)/python36"

在phpStudy软件中点击`其他选项菜单/打开配置文件/httpd-conf`，把这三行内容复制到到LoadModule最后的部分（应该也可以复制到整个文件的最后部分）。

### 3.2.3 部署django项目路径到apache
同样，在apache的http.conf末尾添加下面的内容。目录不同，请对照自己的项目做相应更改。
```text
#指定website的wsgi.py配置文件路径
WSGIScriptAlias / C:/Users/Administrator/Desktop/WebServer/_180524_BlogRayiooo/mysite/wsgi.py
#指定项目路径
WSGIPythonPath  C:/Users/Administrator/Desktop/WebServer/_180524_BlogRayiooo
<Directory C:/Users/Administrator/Desktop/WebServer/_180524_BlogRayiooo/mysite>
    <Files wsgi.py>
        Require all granted
        setHandler wsgi-script
    </Files>
</Directory>
```

### 3.2.4 wsgi.py配置
在项目的wsgi.py文件中`import os`后添加如下代码。
```python
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
```

### 3.2.5 配置完成
在phpStudy中重启apache，从本地（127.0.0.1）和外网（服务器地址）分别访问，查看是否配置成功。

如果出现`HTTP 500 - Internal server error`错误，在apache/logs/error.log中查看错误原因。

如果出现`DisallowedHost at /`错误，就在项目的settings.py文件下做出更改：
```python
ALLOWED_HOSTS = ['*']
```

最终访问成功，只不过在admin页面中缺失了css文件。

![login.png](https://i.loli.net/2018/05/27/5b0a6f92d3fc5.png)

## 3.3 静态文件配置
参考文档：[django static文件的引入方式](http://www.cnblogs.com/yangxiaolan/p/5826661.html) / [django静态文件配置](https://www.cnblogs.com/starof/p/4682812.html)

静态文件配置就是为了让用户请求时django服务器能找到静态文件返回。

首先要理解几个概念：

>* 媒体文件：用户上传的文件
>* 静态文件：css，js，image等
>* 开发环境：使用django内置服务器处理静态文件
>* 生产环境：使用apache2/nginx服务器处理静态文件映射

所以在配置时要分清楚开发环境还是生产环境。为了在生产环境中也能使用到静态文件，我们进行以下配置。

### 3.3.1 settings.py配置
在settings.py中配置如下：

```python
STATIC_URL = '/static/'

# 总的static目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 放各个app的static目录及公共的static目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
    os.path.join(BASE_DIR, 'blog/static'),
]
```

### 3.3.2 收集静态文件到static目录
在cmd中运行`python manage.py collectstatic`，即可将admin的静态文件收集到static目录下。

# 参考资料
[django 快速搭建blog](https://www.cnblogs.com/fnng/p/3737964.html)

[django数据库错误相关问题](https://blog.csdn.net/pipisorry/article/details/45727309)

[windows 下 apache 部署 django python3.6](https://blog.csdn.net/u012846792/article/details/77712958)

[django static文件的引入方式](http://www.cnblogs.com/yangxiaolan/p/5826661.html)

[django静态文件配置](https://www.cnblogs.com/starof/p/4682812.html)

[django settings最佳配置](http://www.cnblogs.com/bergus/p/4423681.html)
