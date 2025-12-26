from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 注册成功后自动登录，然后回主页
            login(request, new_user)
            return redirect('blogs:index')

    # 显示空表单或错误表单
    context = {'form': form}
    return render(request, 'registration/register.html', context)