# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from import_export import resources
from apps.quotation.models import Company, Goods, Type, Unit, Position_type, Warranty_policy, Service, Terms_of_payment, \
    Delivery_time, Delivery_way,Rate,Validity_period


class GoodsResource(resources.ModelResource):
    # def __init__(self):
    #     super(GoodsResource, self).__init__()
    #     field_list = get_model('apps.quotation', 'Goods')._meta.fields
    #     # 应用名与模型名
    #     self.verbose_name_dict = {}
    #     # 获取所有字段的verbose_name并存放在verbose_name_dict字典里
    #     for i in field_list:
    #         self.verbose_name_dict[i.name] = i.verbose_name
    #
    # def get_export_fields(self):
    #     fields = self.get_fields()
    #     # 默认导入导出field的column_name为字段的名称
    #     # 这里修改为字段的verbose_name
    #     for field in fields:
    #         field_name = self.get_field_name(field)
    #         if field_name in self.verbose_name_dict.keys():
    #             field.column_name = self.verbose_name_dict[field_name]
    #             # 如果设置过verbose_name，则将column_name替换为verbose_name
    #             # 否则维持原有的字段名
    #     return fields

    class Meta:
        model = Goods
        # skip_unchanged = True
        # report_skipped = True
        import_id_fields = ('id',)
        # export_id_fields = ('id',)

        fields = (
            'id',
            'name',
            'type',
            'unit',
            'price',
        )
        # 白名单

        exclude = (
            'add_time',

        )
        # 黑名单


class CompanyAdmin(object):
    list_display = ['title', 'ein_no', 'address', 'tel', 'bank_name', 'bank_account', ]
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]
    list_export = ['xls', 'xml', 'json']


class GoodsAdmin(object):
    list_display = ['name', 'unit', 'type', 'nickname', 'price', 'meno', 'add_time']
    search_fields = ['name', 'nickname']
    list_filter = ['name', ]
    list_editable = ['name', ]
    import_export_args = {
        'import_resource_class': GoodsResource,
        # 'export_resource_class': GoodsResource,
    }
    # export_export_args = {
    #     # 'import_resource_class': GoodsResource,
    #     'export_resource_class': GoodsResource,
    # }


class TypeAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class UnitAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class Position_typeAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class Warranty_policyAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class ServiceAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class Terms_of_paymentAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class Delivery_timeAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]


class Delivery_wayAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]


class RateAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]


class Validity_periodAdmin(object):
    list_display = ['title', 'add_time']
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]


xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Unit, UnitAdmin)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Position_type, Position_typeAdmin)
xadmin.site.register(Warranty_policy, Warranty_policyAdmin)
xadmin.site.register(Service, ServiceAdmin)
xadmin.site.register(Terms_of_payment, Terms_of_paymentAdmin)
xadmin.site.register(Delivery_time, Delivery_timeAdmin)
xadmin.site.register(Delivery_way, Delivery_wayAdmin)
xadmin.site.register(Rate, RateAdmin)
xadmin.site.register(Validity_period, Validity_periodAdmin)
