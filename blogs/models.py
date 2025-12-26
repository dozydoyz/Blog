from django.db import models
from django.contrib.auth.models import User # 引入User模型 (这是为了19-5)

# 这里是定义博客文章的地方
class BlogPost(models.Model):
    # 19.1基础功能部分
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 19.5 新增功能部分
    # 给文章加作者，关联到系统自带的User表
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # 简单返回标题
        return self.title