# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from import_export import resources
from apps.documents.models import Quotation_goods,Quotation_info



class Quotation_infoAdmin(object):
    list_display = ['customer', 'add_time']
    search_fields = ['customer', ]
    list_filter = ['customer', ]
    list_editable = ['customer', ]

xadmin.site.register(Quotation_info, Quotation_infoAdmin)
