# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from import_export import resources
from apps.documents.models import Quotation_goods,Quotation_info



class Quotation_infoAdmin(object):
    list_display = ['qid','customer','contact','delivery_time','delivery_way','rate',
                    'terms_of_payment','warranty_policy','service','validity_period','meno', 'add_time']
    search_fields = ['customer', ]
    list_filter = ['customer', ]
    list_editable = ['customer', ]

xadmin.site.register(Quotation_info, Quotation_infoAdmin)


# adminx.py
from xadmin.views.base import CommAdminView
from apps.documents.models import change_into,change_out


class ChangeIntoAdmin(object):
    # 指向自定义的页面
    object_list_template = 'change_into.html'

    # 重写方法，把要展示的数据更新到 context
    def get_context(self):
        context = CommAdminView.get_context(self)

        bill_message = Quotation_info.objects.all()
        context.update(
            {
                'title': '转入分析',
            }
        )

        return context


class ChangeOutAdmin(object):
    object_list_template = 'change_out.html'

    def get_context(self):
        context = CommAdminView.get_context(self)

        bill_message = Quotation_info.objects.all()
        context.update(
            {
                'title': '转出分析',
                'bill_message': bill_message,
            }
        )

        return context

xadmin.site.register(change_into, ChangeIntoAdmin)
xadmin.site.register(change_out, ChangeOutAdmin)
