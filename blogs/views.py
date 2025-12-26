from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogForm

#主页显示所有文章
def index_view(request):
    # 按时间降序排，新的在前面
    blogs = BlogPost.objects.order_by('-date_added')
    # 存到字典里传给网页
    context = {'all_blogs': blogs}
    return render(request, 'blogs/index.html', context)

#  新建文章 
@login_required 
def add_view(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        # 提交数据
        form = BlogForm(data=request.POST)
        if form.is_valid():
            # 要求填owner
            new_obj = form.save(commit=False)
            new_obj.owner = request.user # 把当前登录的人设为作者
            new_obj.save()
            return redirect('blogs:index') # 这里的名字对应urls.py里的name

    context = {'form': form}
    return render(request, 'blogs/add_blog.html', context)

#  编辑文章
@login_required 
def edit_view(request, blog_id):
    # 根据id找文章
    blog = get_object_or_404(BlogPost, id=blog_id)
    # 如果当前登录的用户不是文章的作者就报错
    if blog.owner != request.user:
        raise Http404 

    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        # 提交修改
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)