from django.db import models
# from rbac.models import UserInfo as rabcuserinfo
from apps.users.models import BaseModel, UserProfile


class Company(BaseModel):
    title = models.CharField(max_length=32, unique=True, verbose_name='乙方公司')
    ein_no = models.CharField(max_length=18, verbose_name='税号')
    address = models.CharField(max_length=64, verbose_name='地址')
    tel = models.CharField(max_length=13, verbose_name='电话')
    bank_name = models.CharField(max_length=32, verbose_name='开户银行')
    bank_account = models.CharField(max_length=32, verbose_name='银行账号')

    class Meta:
        verbose_name = '公司名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Supplier(models.Model):  # 供应商
    name = models.CharField(max_length=64, verbose_name='供应商', unique=True)
    advantage = models.CharField(max_length=64, verbose_name='优势品牌', blank=True,null=True)
    contact = models.CharField(max_length=64, verbose_name='联系信息',blank=True,null=True )
    meno = models.CharField(max_length=128, verbose_name='备注',blank=True,null=True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'

class Brand(models.Model):
    name = models.CharField(max_length=24, verbose_name='品牌')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'

class Type(BaseModel):  # 货品类别
    name = models.CharField(max_length=24, verbose_name='货品类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '货品类别'
        verbose_name_plural = verbose_name


class Unit(BaseModel):  # 货品单位
    name = models.CharField(max_length=24, verbose_name='单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '货品单位'
        verbose_name_plural = verbose_name


class Goods(models.Model):  # 货品资料
    brand = models.ForeignKey(to='Brand', verbose_name='品牌', on_delete=models.CASCADE)
    Gmodel = models.CharField(max_length=64, unique=True, verbose_name='品名规格',default='')
    unit = models.ForeignKey(Unit, verbose_name='单位', default=0,on_delete=models.CASCADE )
    type = models.ForeignKey(Type, verbose_name='分类', default=0, on_delete=models.CASCADE )
    price = models.FloatField(verbose_name='进价', default=0)
    min_price = models.FloatField(verbose_name='最低售价', default=0)
    meno = models.TextField(verbose_name='备注', default='备注信息',blank=True,null=True)
    supplier = models.ForeignKey(to='Supplier', verbose_name='供应商', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='更改日期', auto_now=True)
    user = models.ForeignKey(UserProfile, verbose_name='操作员',on_delete=models.CASCADE, editable=False, null=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品信息'

    def __str__(self):
        return self.Gmodel



class Position_type(BaseModel):
    name = models.CharField(max_length=12, verbose_name='职务')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '职务'
        verbose_name_plural = verbose_name


class Contact(BaseModel):  # 联系人
    name = models.CharField(max_length=12, verbose_name='姓名')
    company = models.ForeignKey(to='Customer', verbose_name='所在公司', on_delete=models.CASCADE,related_name='contact')
    gender_choices = ((0, '男'), (1, '女'),)
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)
    position = models.ForeignKey(Position_type, verbose_name='职务', default='', on_delete=models.CASCADE)
    tel = models.CharField(max_length=24, verbose_name='直线号码')
    phone = models.CharField(max_length=12, verbose_name='手机号码')
    email = models.EmailField(verbose_name='电子邮箱')
    wechat_name = models.CharField(max_length=64, verbose_name='微信')
    meno = models.TextField(max_length=256, verbose_name='联系人备注信息')
    address = models.CharField(max_length=128, verbose_name='送货地址')
    invoice_address = models.CharField(max_length=128, verbose_name='发票地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = verbose_name


class Customer(BaseModel):  # 客户
    name = models.CharField(max_length=64, verbose_name='客户名称', unique=True)
    tel = models.CharField(max_length=24, verbose_name='公司电话', unique=True)
    website = models.CharField(max_length=64, verbose_name='公司网址', )
    ein = models.CharField(max_length=18, verbose_name='税号')
    bank = models.CharField(max_length=18, verbose_name='银行')
    bank_account = models.CharField(max_length=32, verbose_name='银行帐号')
    address_tel = models.CharField(max_length=128, verbose_name='地址电话')
    image = models.ImageField(upload_to='media/customer/%Y', default='media/customer/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name


class Warranty_policy(BaseModel):  # 保修政策
    name = models.CharField(max_length=128, verbose_name='保修政策', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '保修政策'
        verbose_name_plural = verbose_name


class Service(BaseModel):  # 服务政策
    name = models.CharField(max_length=128, verbose_name='服务', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '服务政策'
        verbose_name_plural = verbose_name


class Terms_of_payment(BaseModel):  # 付款方式
    name = models.CharField(max_length=64, verbose_name='付款方式', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '付款方式'
        verbose_name_plural = verbose_name


class Delivery_time(BaseModel):
    title = models.CharField(max_length=32, verbose_name='发货时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '发货时间'
        verbose_name_plural = verbose_name


class Delivery_way(BaseModel):
    title = models.CharField(max_length=32, verbose_name='发货方式')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '发货方式'
        verbose_name_plural = verbose_name


class Rate(BaseModel):
    title = models.CharField(max_length=32, verbose_name='发票税率')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '发票税率'
        verbose_name_plural = verbose_name


class Validity_period(BaseModel):
    title = models.CharField(max_length=32, verbose_name='有效期', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '有效期'
        verbose_name_plural = verbose_name



