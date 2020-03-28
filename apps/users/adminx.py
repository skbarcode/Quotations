# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from apps.users import models
from apps.quotation.models import Goods


class GlobalSittings(object):
    site_title = '苏州斯康_订单管理系统'
    site_footer = '苏州斯康'
    menu_style = 'accordion'
    apps_icons = {
        'quotation': "fa fa-plus-square",
    }
    # 配置应用图标，即一级菜单图标
    global_models_icon = {
        Goods: "fa fa-minus-square",
    }

    # 配置模型图标，即二级菜单图标
    def get_site_menu(self):  # 名称不能改
        return [
            {
                'title': '销售管理',
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '报价单',  # 这里是你菜单的名称
                        'url': '/quotation/',  # 这里填写你将要跳转url
                        'icon': 'fa fa-cny'  # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                    {
                        'title': '销售合同',
                        'url': 'http://www.taobao.com',
                        'icon': 'fa fa-cny'
                    }
                )
            }
        ]



class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSittings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
