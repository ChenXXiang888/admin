from django.contrib import admin
from django.contrib.admin.options import TabularInline
from app01.models import *


class GoodsLibAdmin(admin.ModelAdmin):
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


class GoodsAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'lib_id', 'category_id', 'second_category_id', 'image', 'desc', 'sale_price', 'agent_price', 'cost_price', 'taobao_price', 'kaola_price', 'stock', 'status', 'currency_id', 'currency_name']
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


class GoodsSkuAdmin(admin.ModelAdmin):
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


class GoodsCategoryTabularInline(TabularInline):
    model = GoodsSecondCategory


class GoodsCategoryAdmin(admin.ModelAdmin):
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
    inlines = [GoodsCategoryTabularInline]


class GoodsSecondCategoryAdmin(admin.ModelAdmin):
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


class ExchangeRateAdmin(admin.ModelAdmin):
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


class HotGoodsCategoryAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name']
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


class HotAreaAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name']
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


class HotGoodsAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'category_id', 'area_id', 'image', 'desc']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name', 'category_id', 'area_id']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


class HotGoodsSkuAdmin(admin.ModelAdmin):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'goods_id', 'sku_name', 'taobao_price', 'kaola_price', 'stock']
    # 每页显示多少条
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['sku_name']
    # 右侧栏过滤器
    list_filter = ['sku_name', 'taobao_price', 'kaola_price']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']


admin.site.register(GoodsLib, GoodsLibAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsSku, GoodsSkuAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(GoodsSecondCategory, GoodsSecondCategoryAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(HotGoodsCategory, HotGoodsCategoryAdmin)
admin.site.register(HotArea, HotAreaAdmin)
admin.site.register(HotGoods, HotGoodsAdmin)
admin.site.register(HotGoodsSku, HotGoodsSkuAdmin)

