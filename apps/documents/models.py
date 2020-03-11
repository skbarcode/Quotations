from django.db import models
from apps.users.models import BaseModel
from apps.quotation.models import Customer, Contact, Delivery_way, Delivery_time, Goods, Validity_period, Rate, \
    Terms_of_payment, Warranty_policy, Service


# Create your models here.
class Quotation_info(BaseModel):  # 报价单
    qid = models.CharField(max_length=24, unique=True, verbose_name='单据编号')
    customer = models.ForeignKey(to=Customer, verbose_name='客户名称', on_delete=models.CASCADE)
    contact = models.ForeignKey(to=Contact, verbose_name='联系人', on_delete=models.CASCADE)
    delivery_time = models.ForeignKey(Delivery_time, default=0, verbose_name='交货时间', on_delete=models.CASCADE)
    delivery_way = models.ForeignKey(Delivery_way, default=0, verbose_name='交货方式', on_delete=models.CASCADE)
    rate = models.ForeignKey(Rate, verbose_name='税率', default=0, on_delete=models.CASCADE)
    terms_of_payment = models.ForeignKey(to=Terms_of_payment, verbose_name='付款方式', on_delete=models.CASCADE)
    warranty_policy = models.ForeignKey(to=Warranty_policy, verbose_name='保修政策', on_delete=models.CASCADE)
    service = models.ForeignKey(to=Service, verbose_name='服务条款', on_delete=models.CASCADE, )

    validity_period = models.ForeignKey(Validity_period, default=0, verbose_name='有效期', on_delete=models.CASCADE)
    meno = models.TextField(max_length=256, verbose_name='备注信息')

    class Meta:
        verbose_name = '报价单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s' % (self.customer, self.add_time)


class Quotation_goods(BaseModel):  # 报价单中商品
    order = models.ForeignKey(to=Quotation_info, related_name='skus', verbose_name='订单', on_delete=models.CASCADE)
    sku = models.ForeignKey(Goods, verbose_name='货品名称', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='数量')
    price = models.DecimalField(max_digits=12, decimal_places=4, verbose_name='单价')
    meno = models.CharField(max_length=64, verbose_name='备注')

    class Meta:
        verbose_name = '报价单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s' % (self.order, self.add_time)


class change_into(models.Model):
    class Meta:
        verbose_name = u"转入分析"
        verbose_name_plural = verbose_name
        db_table = 'change_into'

    def __str__(self):
        return self.Meta.verbose_name


class change_out(models.Model):
    class Meta:
        verbose_name = u"转出分析"
        verbose_name_plural = verbose_name
        db_table = 'change_out'

    def __str__(self):
        return self.Meta.verbose_name
