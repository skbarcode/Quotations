# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from apps.users import models
from apps.quotation.models import Goods


class GlobalSittings(object):
    site_title = '斯康后台管理系统'
    site_footer = '斯康在线网'
    menu_style = 'accordion'
    apps_icons = {
        'quotation': "fa fa-plus-square",
    }
    # 配置应用图标，即一级菜单图标
    global_models_icon = {
        Goods: "fa fa-minus-square",
    }

    # 配置模型图标，即二级菜单图标
    def get_site_menu(self):
        return (
            {'title': '单据信息',
             # 'perm': self.get_model_perm(models.UserProfile, 'view'),
             'menus': (
                 {
                     'title': '保修政策',
                     'url': '/admin/quotation/warranty_policy/',
                 },
                 {
                     'title': '服务政策',
                     'url': '/admin/quotation/service/',
                 },
                 {
                     'title': '付款方式',
                     'url': '/admin/quotation/terms_of_payment/',
                 },
                 {
                     'title': '发货时间',
                     'url': '/admin/quotation/delivery_time/',
                 },
                 {
                     'title': '发货方式',
                     'url': '/admin/quotation/delivery_way/',
                 },
                 {
                     'title': '发票税率',
                     'url': '/admin/quotation/rate/',
                 },
                 {
                     'title': '有效期',
                     'url': '/admin/quotation/validity_period/',
                 },
             )
             },
        )


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSittings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
