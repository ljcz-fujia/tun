from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserRecord
from .forms import UserRecordForm

# 登录视图
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('record_list')
        else:
            error_message = "用户名或密码错误，请重试。"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

# 注册视图
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('record_list')
            except IntegrityError as e:
                # 处理用户名重复的情况
                if 'UNIQUE constraint failed' in str(e):
                    error_message = "该用户名已被使用，请选择其他用户名。"
                else:
                    error_message = f"数据库插入错误: {str(e)}"
            except Exception as e:
                # 处理其他未知异常
                error_message = f"发生未知错误: {str(e)}"
        else:
            error_message = "两次输入的密码不一致，请重新输入。"
        return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

# 登出视图
def user_logout(request):
    logout(request)
    return redirect('user_login')

# 记录列表视图，需要用户登录才能访问
@login_required
def record_list(request):
    if request.method == 'POST':
        form = UserRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('record_list')
    else:
        form = UserRecordForm()
    records = UserRecord.objects.filter(user=request.user).order_by('-id')
    return render(request, 'record_list.html', {'records': records, 'form': form})

# 编辑记录视图，需要用户登录才能访问
@login_required
def edit_record(request, record_id):
    record = UserRecord.objects.get(id=record_id, user=request.user)
    if request.method == 'POST':
        form = UserRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = UserRecordForm(instance=record)
    return render(request, 'record_list.html', {'form': form, 'record': record})

# 删除记录视图，需要用户登录才能访问
@login_required
def delete_record(request, record_id):
    record = UserRecord.objects.get(id=record_id, user=request.user)
    record.delete()
    return redirect('record_list')