# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from import_export import resources
from apps.documents.models import Quotation_goods, Quotation_info
from xadmin.views.base import CommAdminView


class Quotation_infoAdmin(object):
    list_display = ['qid', 'customer', 'contact', 'delivery_time', 'delivery_way', 'rate',
                    'terms_of_payment', 'warranty_policy', 'service', 'validity_period', 'meno', 'add_time']
    search_fields = ['customer', ]
    list_filter = ['customer', ]
    list_editable = ['customer', ]
    object_list_template = 'template.html'

    def get_context(self):
        context = CommAdminView.get_context(self)

        info = Quotation_info.objects.all()
        print(info.customer)
        context.update(
            {
                'title': '报价单',
            }
        )

        return context







xadmin.site.register(Quotation_info, Quotation_infoAdmin)
