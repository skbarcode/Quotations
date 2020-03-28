# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from import_export import resources
from apps.quotation.models import Company, Goods, Type, Unit, Position_type, Warranty_policy, Service, Terms_of_payment, \
    Delivery_time, Delivery_way, Rate, Validity_period, Customer, Contact,Brand,Supplier
from xadmin.layout import Fieldset, Main, Side, Row


class CompanyAdmin(object):
    list_display = ['title', 'ein_no', 'address', 'tel', 'bank_name', 'bank_account', ]
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_editable = ['title', ]
    list_export = ['xls', 'xml', 'json']


class GoodsResources(resources.ModelResource):
    class Meta:
        model = Goods


class GoodsAdmin(object):
    import_export_args = {'import_resource_class': GoodsResources, 'export_resource_class': GoodsResources}

    list_display = (
        'brand', 'Gmodel', 'unit', 'type', 'price', 'min_price', 'meno', 'supplier', 'user', 'date',)
    search_fields = ('Gmodel', 'meno')
    list_display_links = ('brand', 'Gmodel', 'meno', 'unit', 'type', 'price', 'min_price',)
    list_filter = ('brand', 'type')
    list_per_page = 15
    resource_class = GoodsResources
    model_icon = 'fa fa-map'
    # show_all_rel_details =['brand','unit','type']
    list_editable = ['price','min_price','meno']


    def get_form_layout(self):

        self.form_layout = (
            Main(
                Fieldset('基础信息',
                         'Gmodel',
                         Row('price', 'min_price')
                         # css_class='unsort no_title'
                         ),
                Fieldset('备注信息',
                         "meno",
                         ),
            ),
            # Side(
            #     Fieldset(_('Status'),
            #              'is_active', 'is_staff', 'is_superuser',
            #              ),
            # )
            Side('选择项目',
                 'brand', 'supplier', 'type', 'unit',

                 ),
        )

        return super(GoodsAdmin, self).get_form_layout()

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()


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


class CustomerAdmin(object):
    list_display = ['name', 'tel', 'contact', 'add_time']
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]


class ContactAdmin(object):
    list_display = ['name', 'company', 'position', 'phone', 'add_time']
    search_fields = ['name', 'company', 'position', 'phone']
    list_filter = ['name', 'company', 'position', 'phone']
    list_editable = ['name', 'company']


class SupplierAdmin(object):
    list_display = ['id', 'name', 'advantage', 'meno', 'contact', ]
    search_fields = ['name', 'contact', 'advantage']
    list_filter = ['name', 'contact', 'advantage']
    # list_editable =['name','desc']
    model_icon = 'fa fa-users'


class BrandAdmin(object):
    list_display = ['id', 'name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]
    list_editable = ['name', ]
    model_icon = 'fa fa-superpowers '


xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Supplier, SupplierAdmin)
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
xadmin.site.register(Customer, CustomerAdmin)
xadmin.site.register(Contact, ContactAdmin)
