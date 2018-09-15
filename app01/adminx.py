import xadmin
from xadmin import views
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


class GoodsSkuInline(object):
    model = GoodsSku
    extra = 0


# class GoodsAdmin(admin.ModelAdmin):
class GoodsAdmin(object):
    # 定义要在后台显示哪些字段
    list_display = ['id', 'name', 'lib_id', 'category_id', 'second_category_id', 'image', 'desc', 'sale_price', 'agent_price', 'cost_price', 'taobao_price', 'kaola_price', 'stock', 'status', 'currency_id', 'currency_name']
    # 每页显示多少条
    list_per_page = 2
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True
    # 搜索区域名称
    search_fields = ['name']
    # 右侧栏过滤器
    list_filter = ['name', 'category_id', 'second_category_id']
    # 要在编辑界面编辑哪些字段
    # fields = ['parent', 'title']
    inlines = [GoodsSkuInline]


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


class GoodsCategoryInline(object):
    model = GoodsSecondCategory
    extra = 0


class HotGoodsSkuInline(object):
    model = HotGoodsSku
    extra = 0


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
    inlines = [GoodsCategoryInline]


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


# class GlobalSetting1(object):
#     site_title = "代购小助理后台管理系统"
#     # site_footer = '后台管理系统'  # 设置脚标题
#     menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class HotGoodsCategoryAdmin(object):
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


class HotAreaAdmin(object):
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


class HotGoodsAdmin(object):
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
    inlines = [HotGoodsSkuInline]


class HotGoodsSkuAdmin(object):
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


class GlobalSetting(object):
    site_title = "代购小助理后台管理系统"
    # site_footer = '后台管理系统'  # 设置脚标题
    menu_style = 'accordion'

    # 菜单设置
    def get_site_menu(self):
        return (
            {'title': '商品分类管理', 'perm': self.get_model_perm(GoodsLib, 'change'), 'menus': (
                {'title': '商品库管理', 'url': self.get_model_url(GoodsLib, 'changelist')},
                {'title': '商品管理', 'url': self.get_model_url(Goods, 'changelist')},
                {'title': '商品规格', 'url': self.get_model_url(GoodsSku, 'changelist')},
            )},
            {'title': '分类管理', 'perm': self.get_model_perm(GoodsCategory, 'change'), 'menus': (
                {'title': '一级分类管理', 'url': self.get_model_url(GoodsCategory, 'changelist')},
                {'title': '一级分类管理', 'url': self.get_model_url(GoodsSecondCategory, 'changelist')},
                {'title': '货币汇率管理', 'url': self.get_model_url(ExchangeRate, 'changelist')},
            )},
            {'title': '热销品管理', 'perm': self.get_model_perm(HotGoods, 'change'), 'menus': (
                {'title': '热销商品管理', 'url': self.get_model_url(HotGoods, 'changelist')},
                {'title': '热销商品规格管理', 'url': self.get_model_url(HotGoodsSku, 'changelist')},
                {'title': '热销地区分类管理', 'url': self.get_model_url(HotGoodsCategory, 'changelist')},
            )},
            {'title': '国家地区管理', 'perm': self.get_model_perm(HotArea, 'change'), 'menus': (
                {'title': '国家地区管理', 'url': self.get_model_url(HotArea, 'changelist')},
            )},
        )


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
# # xadmin.site.register(views.CommAdminView, GlobalSetting1)
xadmin.site.register(GoodsLib, GoodsLibAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsSku, GoodsSkuAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(GoodsSecondCategory, GoodsSecondCategoryAdmin)
xadmin.site.register(ExchangeRate, ExchangeRateAdmin)
xadmin.site.register(HotGoodsCategory, HotGoodsCategoryAdmin)
xadmin.site.register(HotArea, HotAreaAdmin)
xadmin.site.register(HotGoods, HotGoodsAdmin)
xadmin.site.register(HotGoodsSku, HotGoodsSkuAdmin)

