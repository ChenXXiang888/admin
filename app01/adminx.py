import xadmin
# from django.contrib import admin
from django.contrib.admin.options import TabularInline
from app01.models import *


# class GoodsLibAdmin(admin.ModelAdmin):
class GoodsLibAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'saler_uid', 'connect_lib', 'status', 'type']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter =['name']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


# class GoodsAdmin(admin.ModelAdmin):
class GoodsAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'lib_id', 'category_id', 'second_category_id', 'image', 'desc', 'sale_price', 'agent_price', 'cost_price', 'stock', 'status', 'currency_id', 'currency_name']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name', 'category_id', 'second_category_id']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


# class GoodsSkuAdmin(admin.ModelAdmin):
class GoodsSkuAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'sku_name', 'sale_price', 'agent_price', 'cost_price', 'stock', 'status', 'goods_id']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['sku_name']
    # 右侧栏过滤器
    list_filter = ['sku_name']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


# class GoodsCategoryTabularInline(TabularInline):
#     model = GoodsSecondCategory


# class GoodsCategoryAdmin(admin.ModelAdmin):
class GoodsCategoryAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'saler_uid', 'status']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name']
    # 要在编辑界面编辑哪些字段
    # fields = ['name']
    # inlines = [GoodsCategoryTabularInline]


# class GoodsSecondCategoryAdmin(admin.ModelAdmin):
class GoodsSecondCategoryAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'status', 'parent_id']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


# class ExchangeRateAdmin(admin.ModelAdmin):
class ExchangeRateAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'rate']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


# class GlobalSetting(object):
#     site_title = '后台管理系统'   # 设置头标题
#     # site_footer = '后台管理系统'  # 设置脚标题
#     menu_style = 'accordion'
#
#
# xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(GoodsLib, GoodsLibAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsSku, GoodsSkuAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsSecondCategory, GoodsSecondCategoryAdmin)
xadmin.site.register(ExchangeRate, ExchangeRateAdmin)

