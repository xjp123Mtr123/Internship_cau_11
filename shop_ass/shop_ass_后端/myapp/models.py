from django.db import models
from django.utils import timezone

class User(models.Model):
    # id
    # 创建用户模型 int text date
    # 字段名
    objects = None
    name = models.CharField("用户名", max_length=50, default='', null=False)
    sname = models.CharField("真实姓名", max_length=50, default='', null=False)
    password = models.CharField("密码", max_length=50, default='', null=False)
    role = models.CharField("角色", max_length=50, default='', null=False)
    bio = models.CharField("个人介绍", max_length=500, default='', null=True)
    signature = models.CharField("个性签名", max_length=50, default='', null=True)
    english_name = models.CharField("英文名", max_length=50, default='', null=True)
    phone = models.CharField("手机号码", max_length=50, default='', null=True)
    avatar = models.CharField("头像url", max_length=200, default='', null=True)
    skills = models.CharField("职业技能", max_length=50, default='', null=True)
    uid = models.CharField("编号", max_length=50, default='', null=True)
    status = models.CharField("状态", max_length=50, default='', null=True)
    email = models.EmailField("邮箱", max_length=100, unique=True, null=False)
    sex = models.CharField("性别", max_length=50, default='', null=True)
    school = models.CharField("地区", max_length=50, default='', null=True)


# 用户日志类
class log(models.Model):
    name = models.CharField("用户名", max_length=50, default='', null=False)
    time = models.CharField("登陆时间", max_length=50, default='', null=False)

# 人工客服
class Email(models.Model):
    recipient = models.CharField(max_length=200, verbose_name="收件人")
    subject = models.CharField(max_length=200, verbose_name="主题")
    body = models.TextField(verbose_name="正文")
    sent_time = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")
    sender = models.CharField(max_length=200, verbose_name="发件人")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "邮件"
        verbose_name_plural = "邮件"


 # 设置问答问题

class Question(models.Model):
    title = models.CharField("问题", max_length=200)
    description = models.TextField("问题描述")

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField("答案")

    def __str__(self):
        return f"Answer to {self.question.title}"

# 摊主
from django.db import models

class wx_user(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

# 进货信息
class PurchaseInfo(models.Model):
    username = models.CharField("用户名", max_length=50)
    purchase_time = models.DateTimeField("进货时间", auto_now_add=True)
    category = models.CharField("商品类别", max_length=50)
    product_name = models.CharField("商品名称", max_length=100)
    quantity = models.IntegerField("商品数量")
    price = models.DecimalField("商品价格", max_digits=10, decimal_places=2)

# 库存信息
class StockInfo(models.Model):
    username = models.CharField("用户名", max_length=50)
    category = models.CharField("商品类别", max_length=50)
    product_name = models.CharField("商品名称", max_length=100)
    quantity = models.IntegerField("商品数量")
    price = models.DecimalField("商品价格", max_digits=10, decimal_places=2)

# 销售模型
from django.db import models

class SalesRecord(models.Model):
    username = models.CharField("用户名", max_length=50)
    product_name = models.CharField("商品名称", max_length=100)
    quantity = models.IntegerField("销售数量")
    sale_price = models.DecimalField("售价", max_digits=10, decimal_places=2)
    cost_price = models.DecimalField("成本价", max_digits=10, decimal_places=2)
    sale_time = models.DateTimeField("销售时间", auto_now_add=True)

    @property
    def total_revenue(self):
        return self.quantity * self.sale_price

    @property
    def total_cost(self):
        return self.quantity * self.cost_price

    @property
    def profit(self):
        return self.total_revenue - self.total_cost

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"

# 额外的项目
class FinancialRecord(models.Model):
    username = models.CharField("用户名", max_length=50)
    item_name = models.CharField("项目名称", max_length=100)
    amount = models.DecimalField("金额", max_digits=10, decimal_places=2)
    record_time = models.DateTimeField("记录时间", auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.amount}"
