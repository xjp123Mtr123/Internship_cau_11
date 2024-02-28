from django.urls import path
from .import views
from myapp import views
urlpatterns =[
    # 首页
    path('index', views.index),
    # 登录
    path('login', views.login),
    # 退出登录
    path('log_out', views.log_out),
    # 注册
    path('regist', views.regist),
    # 系统的登录日志
    path('login_log', views.login_log),
    # 用户管理
    path('user_info', views.user_info),
    # 删除用户
    path('user_delete/<str:username>/<str:password>', views.user_delete),
    # 修改用户
    path('user_alter/<str:username>/<str:password>', views.user_alter),
    # 创建信息 guest_profile_edit
    path('guest_profile_edit', views.guest_profile_edit),
    # 完善信息 guest_profile_edit_upload
    path('guest_profile_edit_upload', views.guest_profile_edit_upload),
    # 首页
    path('guest_index', views.guest_index),
    # 信息展示
    path('guest_profile_display', views.guest_profile_display),
    # 测试页面
    path('test', views.test),
    # 找回密码
    path('reset_password', views.reset_password),
    # 修改密码
    path('change_password/<int:user_id>', views.change_password),
    # 业务逻辑
    # 用户管理
    path('manage_users', views.manage_users),
    path('create_user', views.create_user),
    path('update_user/<int:user_id>', views.update_user),
    path('delete_user/<int:user_id>', views.delete_user),
    # 邮件发送
    path('email_editor', views.email_editor),
    # 邮件删除
    path('email_manage/<int:id>', views.email_manage),
    # 邮件展示
    path('email_presentation', views.email_presentation),
    # 邮件单条展示email_single_presentation
    path('email_single_presentation', views.email_single_presentation),
    # 详情 watch
    path('watch/<int:id>', views.watch),
    # 管理员设置问题
    path('upload_question', views.upload_question),
    path('display_questions', views.display_questions),
    path('upload_answer/<int:question_id>',views.upload_answer),
    # 管理问题和答案
    path('manage_questions', views.manage_questions),
    path('delete_question/<int:question_id>', views.delete_question),
    # djframework的URL
    # 小程序登录
    path('wx_login/', views.LoginView.as_view()),
    # 小程序注册
    path('wx_register/',views.RegisterView.as_view()),
    # 查看库存
    path('wx_GetStockListView/', views.GetStockListView.as_view()),
    # 搜索库存
    path('wx_SearchStockView/', views.SearchStockView.as_view()),
    # 添加进货
    path('wx_AddPurchaseView/', views.AddPurchaseView.as_view()),
    path('purchase_list', views.purchase_list),
    path('stock_list', views.stock_list),
    path('download_purchase_csv', views.download_purchase_csv),
    # 库存信息的CRUD
    path('wx_StockListView/', views.StockListView.as_view()),
    path('wx_StockDetailView/<int:pk>/', views.StockDetailView.as_view()),
    path('wx_UpdateStockView/', views.UpdateStockView.as_view()),
    path('wx_DeleteStockView/', views.DeleteStockView.as_view()),
    # 销售
    path('wx_GetSalesRecordView/', views.GetSalesRecordView.as_view()),
    path('wx_AddSalesRecordView/', views.AddSalesRecordView.as_view()),
    # 额外支出
    path('wx_GetFinancialRecordView/', views.GetFinancialRecordView.as_view()),
    path('wx_AddFinancialRecordView/', views.AddFinancialRecordView.as_view()),
    path('wx_UpdateUserInfoView/', views.UpdateUserInfoView.as_view()),
    path('download_purchase_info', views.download_purchase_info),
    path('download_stock_info', views.download_stock_info),
    path('download_sales_record', views.download_sales_record),
    path('download_financial_record', views.download_financial_record),
    path('report', views.report),

]
# 出现86的唯一原因是 middleware在拦截