# Blog应用程序设计

一款基于 Python Web 框架（`Django`）与前端工具库（`Bootstrap4`）开发的个人博客系统。本项目实现了从基础的文章发布与展示，到用户权限管理的功能。

## 目录

*   简介
*   功能特性
*   运行环境与依赖
*   运行流程说明
*   项目结构

## 功能特性

*   __基础博客功能 (19.1)__  
    主页能够自动从数据库读取文章，并严格按照发布时间倒序排列，同时提供发布新文章与编辑现有文章的表单界面。
*   __用户身份认证 (19.5)__  
    构建了独立的用户系统。实现了用户的注册、登录与注销逻辑。
*   __数据权限保护 (19.5)__  
    实现了严格的后端权限校验。系统通过外键关联确保每篇文章归属特定作者：
    *   __前端隔离__：非作者用户无法看到“修改”按钮。
    *   __后端拦截__：非作者用户强行访问编辑 URL 会触发报错。


## 运行环境与依赖

所需依赖：

*   Python 3.x
*   Django >= 5.0
*   django-bootstrap4
*   SQLite3 (内置)

安装依赖：

```
pip install -r requirements.txt
```

## 运行流程说明

请按照以下步骤初始化并启动服务器：

1.  __安装依赖__
    
    ```
    pip install -r requirements.txt
    ```
    
2.  __初始化数据库__  
    （重建数据库结构与表）
    
    ```
    python manage.py makemigrations blogs
    python manage.py makemigrations users
    python manage.py migrate
    ```
    
3.  __创建管理员账户__  
    （用于访问后台管理系统）
    
    ```
    python manage.py createsuperuser
    ```
    
4.  __启动服务器__  
    启动成功后，请访问 `http://127.0.0.1:8000/`
    
    ```
    python manage.py runserver
    ```
    

## 项目结构

```
Blog/
│── manage.py           # 项目管理与启动入口
│── requirements.txt    # 依赖包列表
│── blog_project/       # 项目全局配置
│   │── settings.py     # 应用注册与数据库配置
│   │── urls.py         # 全局路由分发
│── blogs/              # 核心博客应用
│   │── models.py       # BlogPost 数据模型定义
│   │── views.py        # 文章列表、发布与权限校验逻辑
│   │── forms.py        # 表单定义与汉化
│── users/              # 用户认证应用
│   │── views.py        # 注册逻辑实现
│   │── urls.py         # 认证路由配置
│── templates/          # 全局模板目录
    │── blogs/          # 博客页面 (index, base, edit)
    │── registration/   # 认证页面 (login, register)
```
