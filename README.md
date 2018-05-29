
这是一个Django博客。

`BlogRayiooo` = `python3.6/32位` + `apache2.4/32位` + `MySQL` + `win10 server`

[更方便地查看文档](https://www.zybuluo.com/rayiooo/note/1155365)

|Author|爱吃大板|
|---|---|
|Email|rayiooo@foxmail.com|

# 1 python库
* django
* pymysql
* mod_wsgi

# 2 软件工具
* PyCharm（IDE）
* phpStudy（Apache2.4/32位、MySQL等环境的一键配置工具，超好用！）

# 3 搭建步骤
## 3.1 准备工作
首先我们要建立一个django工程，并使得它在本地能够被访问。

### 3.1.1 新建项目
在PyCharm的`File/New Project`中新建一个Django项目。

### 3.1.2 修改数据库类型
Django默认使用了python自带的SQLite数据库。我在这里修改它，当然你也可以使用SQLite进行存储数据。

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
要想登录django自带的admin后台，必须要有帐号，接下来创建超级管理员帐号。[↻](https://www.cnblogs.com/fnng/p/3737964.html)

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

输入之前设定的账号密码，即可进入django自带的数据库管理界面。

## 3.2 部署服务器端
特别参考：[windows 下 apache 部署 django python3.6](https://blog.csdn.net/u012846792/article/details/77712958)

**特别强调注意**的是：apache 的位制和python的位制必须一致（即apache 32位的就只能安装python 32位的，64位也一样）网上很多教程没强调这一点，导致后续的很多工作白费，还找不到问题所在！

因此如果使用phpStudy的apache 32位，就必须使用python 32位。当然你也可以下载独立的Apache进行相应操作。

部署服务器端的时候，需要将之前在开发时进行的测试操作重新执行一遍。

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
参考文档：[django静态文件配置](https://www.cnblogs.com/starof/p/4682812.html)

静态文件配置就是为了让用户请求时django服务器能找到静态文件并返回。在开发时，静态文件存储在python安装目录下，但是在服务器上运行django时则无法从该目录获取静态文件，就会出现css缺失而导致3.2.5中所述情况发生。

首先要理解几个概念：

>* 媒体文件：用户上传的文件
>* 静态文件：css，js，image等
>* 开发环境：使用django内置服务器处理静态文件
>* 生产环境：使用apache2/nginx服务器处理静态文件映射

所以在配置时要分清楚开发环境还是生产环境。为了在生产环境中也能使用到静态文件，而不会出现访问时找不到css、js文件的问题，我们进行以下配置。

### 3.3.1 settings.py配置
在settings.py中配置static静态文件夹路径如下：

```python
STATIC_URL = '/static/'

# 总的static目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 放各个app的分static目录及公共的static目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog/static'),
]
```

### 3.3.2 收集静态文件到static目录
在cmd中运行`python manage.py collectstatic`，即可将原本放在python安装目录下的admin的静态文件收集到工程文件夹下的static目录下。

### 3.3.3 配置服务器端apache的httpd.conf
通过Github将本地收集到的static文件们同步到服务器端后，在服务器的apache的httpd.conf文件夹下进行如下配置：

```text
# set static path
Alias /static "C:\Users\Administrator\Desktop\WWW\BlogRayiooo\static"
<Directory "C:\Users\Administrator\Desktop\WWW\BlogRayiooo\static">
  Require all granted 
</Directory>
```

这表示我们将`"C:\Users\Administrator\Desktop\WWW\BlogRayiooo\static"`这个路径的东西映射到网站的`http://我的IP/static`分支下。这时我的http.conf文件里应该是这样的：

![httpconf.png](https://i.loli.net/2018/05/28/5b0ae03124ed2.png)

这段配置应当放到wsgi配置前，以保证载入wsgi时不再缺失static文件。

### 3.3.4 css文件在远端加载成功
重启phpStudy的apach，即可在远端成功加载css文件。（摸爬滚打一下午 + 一晚上终于完成）

## 3.4 设计models.py（数据库表）
每个博客的文章都包含了标题、作者、类型、发布时间、阅读量、文章内容、Url等字段。为了给这些元素建立一个数据库，我们将设计`blog/models.py`文件，并使用django的`migrations`指令和`migrate`指令快速建库。

### 3.4.1 设计blog表
打开`blog/models.py`，定义数据库的结构。了解更多请参阅 [Django Models 文档](https://docs.djangoproject.com/en/1.11/topics/db/models/)

```python
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    id = models.AutoField(primary_key=True, unique=True)


class ArticleType(models.Model):
    type = models.CharField(primary_key=True, unique=True, max_length=10)


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.ForeignKey(ArticleType, on_delete=models.PROTECT)
    content = models.TextField()
    timestamp = models.DateTimeField()
    click = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
```

### 3.4.2 执行数据库同步
利用`python manage.py makemigrations blog`命令可以在`blog/migrations`目录下建立一个migration，例如`0001_initial.py`，在这个文件中根据你规定的models定义了一些建库操作。

因此，接下来执行`python manage.py migrate`指令就可以根据migrations文件夹下的文件执行建库操作。

假如你在本地进行了`makemigrations`，只需将migrations文件夹中的文件同步到服务器端，并在服务器端执行`migrate`指令，即可便捷地完成建库。

```text
D:\Coding Projects\Python\_180524_BlogRayiooo>python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article
    - Create model ArticleType
    - Create model User
    - Add field author to article
    - Add field type to article

D:\Coding Projects\Python\_180524_BlogRayiooo>python manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/2.0/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

### 3.4.3 通过admin.py管理
编写`blog/admin.py`文件如下：
```python
from django.contrib import admin
from blog.models import User, ArticleType, Article


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'E-mail']


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'type', 'content', 'timestamp']


admin.site.register(User, UserAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
```

### 3.4.4 登录Admin后台添加blog

# 参考资料
[django 快速搭建blog](https://www.cnblogs.com/fnng/p/3737964.html)

[django数据库错误相关问题](https://blog.csdn.net/pipisorry/article/details/45727309)

[windows 下 apache 部署 django python3.6](https://blog.csdn.net/u012846792/article/details/77712958)

[django静态文件配置](https://www.cnblogs.com/starof/p/4682812.html)

[django settings最佳配置](http://www.cnblogs.com/bergus/p/4423681.html)

[Django Models 文档](https://docs.djangoproject.com/en/1.11/topics/db/models/)

[使用strapdown.js解析markdown](https://blog.csdn.net/u010351766/article/details/51704958)
