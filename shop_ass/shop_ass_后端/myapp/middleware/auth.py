from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
import re
class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 如果用户访问的是 www.baidu.com，直接允许
        if (request.path_info == "/myapp/wx_message/"
                or request.path_info == "/myapp/wx_login/"
                # wx库存管理
                or request.path_info == "/myapp/wx_UpdateStockView/"
                or request.path_info == "/myapp/wx_DeleteStockView/"

                # wx的销售
                or request.path_info == "/myapp/wx_GetSalesRecordView/"
                or request.path_info == "/myapp/wx_AddSalesRecordView/"

                # 财务管理
                or request.path_info == "/myapp/wx_GetFinancialRecordView/"
                or request.path_info == "/myapp/wx_AddFinancialRecordView/"

                or request.path_info == "/myapp/wx_UpdateUserInfoView/"

                or request.path_info == "/myapp/wx_StockListView/"
                or request.path_info == "/myapp/wx_StockDetailView/"
                or request.path_info == "/myapp/wx_AddPurchaseView/"
                or request.path_info == "/myapp/wx_GetStockListView/"
                or request.path_info == "/myapp/wx_SearchStockView/"
                or request.path_info == "/myapp/wx_register/"
                or request.path_info == "/myapp/login"
                or request.path_info == "/myapp/regist"
                or request.path_info == "/myapp/reset_password"
                or request.path_info == "/myapp/wx_login_framework"

        ):
            # 将session中的info设为空
            request.session["info"] = None
            return

        # 检查URL是否以/myapp/change_password/开始
        if re.match(r'^/myapp/change_password/\d+$', request.path_info):
            request.session["info"] = None
            return

        # 读取浏览器中的session信息 如果能读到 说明已经登陆
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 如果没有登陆过，可以选择弹出提示框或者跳转到登录页面
        # 使用HttpResponse返回一个JavaScript弹窗提示
        return HttpResponse('<script>alert("请先注册或登录!"); window.location.href="/myapp/login";</script>')


