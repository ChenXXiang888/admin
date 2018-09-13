from django.db import models


class GoodsCategory(models.Model):
    """
    商品一级分类
    """
    name = models.CharField(max_length=32, verbose_name='商品一级分类名称')
    saler_uid = models.CharField(max_length=32, verbose_name='创建者uid')
    status = models.IntegerField(default=0, verbose_name='一级分类状态')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "df_goods_category"
        verbose_name = "商品商品一级分类"
        verbose_name_plural = verbose_name


class GoodsSecondCategory(models.Model):
    """
    商品二级分类
    """
    name = models.CharField(max_length=32, verbose_name='商品一级分类名称')
    status = models.IntegerField(default=0, verbose_name='二级分类状态')
    parent_id = models.ForeignKey(GoodsCategory, verbose_name='一级分类id')
    # parent_id = models.IntegerField(default=0, verbose_name='一级分类id')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "df_goods_second_category"
        verbose_name = "商品商品二级分类"
        verbose_name_plural = verbose_name


class GoodsLib(models.Model):
    """
    商品库表
    name 商品库名称
    saler_uid 商品库拥有人
    connect_lib 关联的商品库ID，非关联时该字段为0
    status 状态 0-正常 1-删除
    type 类型 0-普通商品库 1-临时商品库
    """
    name = models.CharField(max_length=16, verbose_name='商品库名称')
    saler_uid = models.CharField(max_length=32, verbose_name='创建者uid')
    connect_lib = models.IntegerField(default=0, verbose_name='关联商品库')
    status = models.IntegerField(default=0, verbose_name='商品库状态')
    type = models.IntegerField(default=0, verbose_name='商品库类型')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "df_goods_lib"
        verbose_name = "商品库"
        verbose_name_plural = verbose_name


class ExchangeRate(models.Model):
    """
    货币汇率表，外币兑人民币
    name 外币货币名称
    rate 汇率
    """
    name = models.CharField(max_length=16, verbose_name='外币货币名称')
    rate = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="汇率")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "df_exchange_rate"
        verbose_name = "货币汇率表"
        verbose_name_plural = verbose_name


class Goods(models.Model):
    """商品规格表
    name 商品名称
    lib_id  所属商品库id
    status 商品状态 0-正常 1-下架 2-删除
    """
    name = models.CharField(max_length=16, verbose_name='商品名称')
    lib_id = models.ForeignKey(GoodsLib, verbose_name='商品库id')
    # category_id = models.IntegerField(default=0, verbose_name='一级分类')
    # second_category_id = models.IntegerField(default=0, verbose_name='二级分类')
    category_id = models.ForeignKey(GoodsCategory, verbose_name='一级分类id')
    second_category_id = models.ForeignKey(GoodsSecondCategory, verbose_name='二级分类id')
    # 头像, 上传的图片保存到media/app01/image目录下
    image = models.ImageField(upload_to='app01/image/', verbose_name="商品图片")
    desc = models.TextField(verbose_name="商品描述", default="", blank=True)
    sale_price = models.IntegerField(default=0, verbose_name='售价')
    agent_price = models.IntegerField(default=0, verbose_name='代理价')
    cost_price = models.IntegerField(default=0, verbose_name='成本价')
    stock = models.IntegerField(default=0, verbose_name='库存')
    status = models.IntegerField(default=0, verbose_name='商品状态')
    currency_id = models.IntegerField(default=0, verbose_name='货币id')
    # currency_name = models.CharField(max_length=16, verbose_name='货币名称')
    currency_name = models.ForeignKey(ExchangeRate, verbose_name='货币名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "df_goods"
        verbose_name = "商品库商品"
        verbose_name_plural = verbose_name


class GoodsSku(models.Model):
    """
    商品规格表
    """
    sku_name = models.CharField(max_length=32, verbose_name='商品规格名称')
    sale_price = models.IntegerField(default=0, verbose_name='售价')
    agent_price = models.IntegerField(default=0, verbose_name='代理价')
    cost_price = models.IntegerField(default=0, verbose_name='成本价')
    stock = models.IntegerField(default=0, verbose_name='库存')
    status = models.IntegerField(default=0, verbose_name='商品规格状态')
    goods_id = models.ForeignKey(Goods, verbose_name='商品id')

    def __str__(self):
        return self.sku_name

    class Meta:
        db_table = "df_goodssku"
        verbose_name = "商品规格表"
        verbose_name_plural = verbose_name






