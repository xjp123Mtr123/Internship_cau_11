from django.shortcuts import render,redirect
from .models import User,log
from datetime import date
from django.shortcuts import redirect
import calendar
from django.http import HttpResponse, HttpResponseRedirect
import time
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # 设置无头后端
import matplotlib.pyplot as plt
# 网页 参数 只能或者说必须含有 request 请求
# get post
# 首页
def index(request):
    if request.method == 'GET':
        return render(request,'index.html',locals())
# 前后端 交互 request 请求 get post
from django.db.models import Avg
# 登录#get post
def login(request):
    if request.method =='GET':
        return render(request, 'login.html', locals())
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # orm 技术
        exists = User.objects.filter(name = username ,password = password).exists()
        if not exists:
            return render(request, 'login.html', locals())
        else:
            times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            log.objects.create(name = username,time=times)
            p = User.objects.filter(name=username, password=password).values('role')[0]['role']
            if username== 'admin':
                # 将用户名写入cookie和session中
                request.session["info"] = {'name': username}
                 #middleware 装饰器

                return redirect('/myapp/index')
            else :
                # 登陆时，check
                # 将用户名写入cookie和session中
                request.session["info"] = {'name': username}
                return redirect('/myapp/guest_index')

# 第三章 功能模块
# 第四章 怎么实线的
# 退出登录

def log_out(request):
    if request.method =='GET':
        return redirect('/myapp/login')
# 中间件
# 注册
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html', locals())
    else:
        a = request.POST['a']  #
        b = request.POST['b']  #
        c = 'guest'  #
        email = request.POST['email']  #
        sname = request.POST['sname']  #
        school = request.POST['school']  #
        sex = request.POST['sex']  #
        phone = request.POST['phone']  #

        exists = User.objects.filter(name=a).exists()
        if exists:
            return HttpResponse('该用户名已被注册')

        # 创建新用户并保存新的字段值
        User.objects.create(
            name=a,
            password=b,
            role=c,
            email=email,
            sname=sname,
            school=school,
            sex=sex,
            phone=phone
        )
        return render(request, 'login.html', locals())

# pip freezen > requirements.txt
# 登录日志
def login_log(request):
    if request.method =='GET':
        info = log.objects.all()
        return render(request,'login_log.html',locals())

# 用户管理
def user_info(request):
    if request.method=='GET':
        info = User.objects.all()
        return render(request, 'user_info.html', locals())

# 用户删除
def user_delete(request,username,password):
    if request.method=='GET':
        a = username
        b = password
        p = User.objects.filter(name=a,password=b)
        p.delete()
        # 使用redirect 可以保证url不会错误
        return redirect('/myapp/login')

# 用户修改
def user_alter(request,username,password):
    a = username
    b = password
    if request.method=='GET':
        info  = User.objects.filter(name=a,password=b)
        return render(request,'user_alter.html',locals())
    elif request.method=='POST':
        a = a
        b = b
        c = request.POST['aa']
        d = request.POST['bb']
        User.objects.filter(name=a, password=b).update(name=c, password=d)
        return redirect('/myapp/login')

# 员工创建信息 guest_profile_edit
def guest_profile_edit(request):
    if request.method=='GET':
        user_name = request.session["info"]['name']
        print('用户信息',user_name)
        user = User.objects.get(name=user_name)
        return render(request, 'guest_profile_edit.html', locals())

# 完善信息
def guest_profile_edit_upload(request):
    if request.method == 'POST':
        bio = request.POST['bio']
        signature = request.POST['signature']
        english_name = request.POST['english_name']
        email = request.POST['email']
        sex = request.POST['sex']
        status = request.POST['status']
        uid = request.POST['uid']

        phone = request.POST['phone']
        skills = request.POST['skills']
        user_name = request.session["info"]['name']
        print('用户信息',user_name)
        user_profile = User.objects.get(name=user_name)
        user_profile.bio = bio
        user_profile.signature = signature
        user_profile.english_name = english_name
        user_profile.email = email
        user_profile.sex = sex
        user_profile.status = status
        user_profile.uid = uid
        user_profile.phone = phone
        # if avatar:
        #     user_profile.avatar = file_path
        user_profile.skills = skills
        user_profile.save()
    return render(request, 'guest_index.html',locals())

# 首页
def guest_index(request):
    if request.method == 'GET':
        return render(request,'guest_index.html',locals())

# 信息展示
def guest_profile_display(request):
    if request.method == 'GET':
        user_name = request.session["info"]['name']
        user = User.objects.get(name=user_name)
        return render(request,'guest_profile_display.html',locals())

# 测试页面
def test(request):
    if request.method == 'GET':
        return render(request,'test.html',locals())


# 找回密码
def reset_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.filter(name=username, email=email).first()
        if user:
            # 如果用户名和邮箱匹配，重定向到密码重置页面
            print(user.id)
            url = '/myapp/change_password'+'/'+str(user.id)
            return redirect(url)
        else:
            # 如果不匹配，返回错误消息
            error_message = "用户名或邮箱不正确"
            return render(request, 'reset_password.html', {'error_message': error_message})
    return render(request, 'reset_password.html')

# 创建密码重置
def change_password(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        new_password = request.POST['new_password']
        user.password = new_password
        user.save()
        return redirect('/myapp/login')  # 重定向到登录页面
    return render(request, 'change_password.html', {'user': user})

# 对用户进行管理
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/manage_users')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/myapp/manage_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('/myapp/manage_users')

from .models import Email
from django.utils import timezone

def email_editor(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']
        sent_time = timezone.now()
        user_name = request.session["info"]['name']
        email = Email(recipient=recipient, subject=subject, body=body, sent_time=sent_time,sender = user_name)
        email.save()

        return redirect('/myapp/guest_index')
    users = User.objects.all()
    return render(request, 'email_editor.html',locals())

# 邮件删除
def email_manage(request,id):
    if request.method == 'GET':
        p = Email.objects.filter(id = id).first()
        p.delete()
        return redirect('/myapp/index')

# 邮件展示
def email_presentation(request):
    if request.method == 'GET':
        info = Email.objects.all()

        return render(request, 'email_presentation.html',locals())


def email_single_presentation(request):
    emails = Email.objects.all()
    subjects = Email.objects.values_list('subject', flat=True).distinct()
    context = {'info': emails, 'subjects': subjects}
    return render(request, 'email_single_presentation.html', context)

def watch(request,id):
    if request.method =='GET':
        email = Email.objects.filter(id = id).first()
        return render(request,'watch.html',locals())

# 设置问题
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def upload_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/index')
    else:
        form = QuestionForm()
    return render(request, 'upload_question.html', {'form': form})

def display_questions(request):
    questions = Question.objects.all()
    return render(request, 'display_questions.html', {'questions': questions})

def upload_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('/myapp/display_questions')
    else:
        form = AnswerForm()
    return render(request, 'upload_answer.html', {'form': form, 'question': question})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def manage_questions(request):
    questions = Question.objects.all()
    return render(request, 'manage_questions.html', {'questions': questions})

def delete_question(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        question.delete()
        return redirect('/myapp/manage_questions')
    else:
        return redirect('/myapp/manage_questions')

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

from django.http import HttpResponse

# 为了简化，暂时禁用CSRF保护
# def wx_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         passwd = request.POST.get('passwd')
#
#         # 检查用户名和密码是否匹配
#         user = User.objects.filter(name=username, password=passwd).first()
#         if user:
#             # 用户名和密码匹配
#             return Response({'status': True, 'message': '注册成功'})
#
#
#         else:
#             # 用户名或密码错误
#             return Response({'status': False})
#     else:
#         return HttpResponse("仅支持POST请求")

from django.http import HttpResponse
from .models import wx_user
# 提前下载 pip install djangorestframework
from rest_framework.views import APIView
from rest_framework.response import Response
# @csrf_exempt
# 小程序登录
class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.query_params)
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        print(username)
        # 检查用户名和密码是否匹配
        user = User.objects.filter(name=username, password=password).first()
        if user:
            return Response({'status': True, 'message': '登录成功'})
        else:
            return Response({'status': False, 'message': '用户名或密码错误'})

# 小程序注册
class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取注册信息
        name = request.query_params.get('name')
        password = request.query_params.get('password')
        phone = request.query_params.get('phone')
        email = request.query_params.get('email')

        # 检查用户名是否已存在
        if User.objects.filter(name=name).exists():
            print('已经存在')
            return Response({'status': False, 'message': '用户名已存在'})
        else:
            # 创建新用户并保存
            User.objects.create(name=name, password=password, phone=phone, email=email)
            print('新创建！')
            return Response({'status': True, 'message': '注册成功'})

        return Response({'status': False, 'message': '注册请求失败'})

def wx_index(request):
    userid = request.GET.get('test_number')
    print(userid)
    return Response({'status': True})
from django.db.models import Q
from .models import StockInfo, PurchaseInfo
# 展示库存列表
class GetStockListView(APIView):
    def get(self, request, *args, **kwargs):
        print('测试是否调用')
        username = request.query_params.get('username')
        print(username)
        stock_list = StockInfo.objects.filter(username=username).values()
        print(stock_list)
        return Response({'status': True, 'stockList': list(stock_list)})

# 展示查找的库存信息
class SearchStockView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        query = request.query_params.get('query')

        # 搜索匹配商品名称或商品类别
        stock_list = StockInfo.objects.filter(
            Q(username=username) &
            (Q(product_name__icontains=query) | Q(category__icontains=query))
        ).values()

        return Response({'status': True, 'stockList': list(stock_list)})
# 添加进货信息
from django.utils import timezone
class AddPurchaseView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        product_name = request.query_params.get('productName')
        category = request.query_params.get('category')
        quantity = int(request.query_params.get('quantity'))
        price = float(request.query_params.get('price'))

        # 添加进货信息
        PurchaseInfo.objects.create(
            username=username,
            category=category,
            product_name=product_name,
            quantity=quantity,
            price=price,
            purchase_time=timezone.now()  # 设置当前时间为进货时间
        )

        # 更新或创建库存信息
        stock, created = StockInfo.objects.get_or_create(
            username=username,
            category=category,
            product_name=product_name,
            defaults={'quantity': quantity, 'price': price}
        )
        if not created:
            stock.quantity += quantity
            stock.save()

        return Response({'status': True, 'message': '进货信息添加成功'})
from django.shortcuts import render
from django.http import HttpResponse
from .models import PurchaseInfo, StockInfo
import csv
from django.core.paginator import Paginator
# 网页端展示数据
def purchase_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        purchases = PurchaseInfo.objects.filter(product_name__icontains=search_query)
    else:
        purchases = PurchaseInfo.objects.all()

    # 分页逻辑
    paginator = Paginator(purchases, 10)  # 每页显示 10 条记录
    page = request.GET.get('page')
    purchases_page = paginator.get_page(page)

    return render(request, 'purchase_list.html', {'purchases': purchases_page})

def stock_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        stocks = StockInfo.objects.filter(product_name__icontains=search_query)
    else:
        stocks = StockInfo.objects.all()

    # 分页逻辑
    paginator = Paginator(stocks, 10)  # 每页显示 10 条记录
    page = request.GET.get('page')
    stocks_page = paginator.get_page(page)

    return render(request, 'stock_list.html', {'stocks': stocks_page})

def download_purchase_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="purchases.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Purchase Time', 'Category', 'Product Name', 'Quantity', 'Price'])
    purchases = PurchaseInfo.objects.all().values_list('username', 'purchase_time', 'category', 'product_name', 'quantity', 'price')
    for purchase in purchases:
        writer.writerow(purchase)
    return response

# 对小程序端的库存实现CRUD
from django.shortcuts import get_object_or_404

class StockListView(APIView):
    def get(self, request, *args, **kwargs):
        print('测试是否调用')
        username = request.query_params.get('username')
        print(username)
        stocks = StockInfo.objects.filter(username=username).values()
        return Response({'status': True, 'stocks': list(stocks)})

class StockDetailView(APIView):
    def get(self, request, pk):
        stock = get_object_or_404(StockInfo, pk=pk)
        return Response({'status': True, 'stock': stock})

class UpdateStockView(APIView):
    def get(self, request, *args, **kwargs):
        pk = request.query_params.get('pk')
        stock = get_object_or_404(StockInfo, pk=pk)
        quantity = request.query_params.get('quantity')
        price = request.query_params.get('price')
        print(quantity)

        if quantity is not None:
            stock.quantity = int(quantity)
        if price is not None:
            stock.price = float(price)
        stock.save()
        return Response({'status': True, 'message': 'Stock updated successfully'})

class DeleteStockView(APIView):
    def get(self, request, *args, **kwargs):
        pk = request.query_params.get('pk')
        stock = get_object_or_404(StockInfo, pk=pk)
        stock.delete()
        return Response({'status': True, 'message': 'Stock deleted successfully'})

# 销售管理
from .models import SalesRecord,FinancialRecord
class GetSalesRecordView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        sales_records = SalesRecord.objects.filter(username=username)
        records = [{
            'product_name': record.product_name,
            'quantity': record.quantity,
            'sale_price': record.sale_price,
            'cost_price': record.cost_price,
            'profit': record.profit  # 新增利润
        } for record in sales_records]
        return Response({'status': True, 'sales_records': records})

class AddSalesRecordView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        product_name = request.query_params.get('product_name')
        quantity = int(request.query_params.get('quantity'))
        sale_price = float(request.query_params.get('sale_price'))
        cost_price = float(request.query_params.get('cost_price'))  # 新增成本价

        SalesRecord.objects.create(
            username=username,
            product_name=product_name,
            quantity=quantity,
            sale_price=sale_price,
            cost_price=cost_price  # 新增成本价
        )
        return Response({'status': True, 'message': 'Sales record added successfully'})

# 额外支出
class GetFinancialRecordView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        financial_records = FinancialRecord.objects.filter(username=username).values()
        return Response({'status': True, 'financial_records': list(financial_records)})

class AddFinancialRecordView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        item_name = request.query_params.get('item_name')
        amount = float(request.query_params.get('amount'))

        FinancialRecord.objects.create(
            username=username,
            item_name=item_name,
            amount=amount
        )
        return Response({'status': True, 'message': 'Financial record added successfully'})

class UpdateUserInfoView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        user = User.objects.get(name=username)
        user.password = request.query_params.get('sname', user.sname)
        # 更新其他字段
        user.save()
        return Response({'status': True, 'message': 'User info updated successfully'})

import csv
from django.http import HttpResponse
from .models import PurchaseInfo, StockInfo, SalesRecord, FinancialRecord

def download_csv(model, filename, headers, data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    writer.writerow(headers)
    for record in data:
        writer.writerow(record)

    return response

def download_purchase_info(request):
    user_name = request.session["info"]['name']
    data = PurchaseInfo.objects.filter(username=user_name).values_list('username', 'purchase_time', 'category', 'product_name', 'quantity', 'price')
    headers = ["用户名", "进货时间", "商品类别", "商品名称", "商品数量", "商品价格"]
    return download_csv(PurchaseInfo, "purchase_info.csv", headers, data)

def download_stock_info(request):
    user_name = request.session["info"]['name']
    data = StockInfo.objects.filter(username=user_name).values_list('username', 'category', 'product_name', 'quantity', 'price')
    headers = ["用户名", "商品类别", "商品名称", "商品数量", "商品价格"]
    return download_csv(StockInfo, "stock_info.csv", headers, data)

def download_sales_record(request):
    user_name = request.session["info"]['name']
    data = SalesRecord.objects.filter(username=user_name).values_list('username', 'product_name', 'quantity', 'sale_price', 'cost_price', 'sale_time')
    headers = ["用户名", "商品名称", "销售数量", "售价", "成本价", "销售时间"]
    return download_csv(SalesRecord, "sales_record.csv", headers, data)

def download_financial_record(request):
    user_name = request.session["info"]['name']
    data = FinancialRecord.objects.filter(username=user_name).values_list('username', 'item_name', 'amount', 'record_time')
    headers = ["用户名", "项目名称", "金额", "记录时间"]
    return download_csv(FinancialRecord, "financial_record.csv", headers, data)

def report(request):
    if request.method == 'GET':
        return render(request,'report.html',locals())