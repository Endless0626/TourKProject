from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    title = models.CharField(max_length=40, verbose_name='留言标题')
    content = models.TextField(verbose_name='留言内容')
    quizDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='提交时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '问答'
        verbose_name_plural = '问答'
        ordering = ('-quizDate', )

class Reply(models.Model):
    replyname = models.CharField(max_length=20, verbose_name='姓名')
    title = models.ForeignKey(Quiz, related_name='replys', verbose_name='回复', on_delete=models.CASCADE, null=True)
    replycontent = models.TextField(verbose_name='回复')
    replyDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='回复时间')

    class Meta:
        verbose_name = '问题回复'
        verbose_name_plural = '问题回复'

class Visa(models.Model):
    title = models.CharField(max_length=100, verbose_name='签证名称')
    city = models.CharField(max_length=20, verbose_name='城市')
    type = models.CharField(max_length=20, verbose_name='签证类型')
    expire = models.CharField(max_length=20, verbose_name='有效期')
    staydays = models.CharField(max_length=20, verbose_name='停留天数')
    number = models.CharField(max_length=20, verbose_name='入境次数')
    order = models.CharField(max_length=20, verbose_name='订单有效期')
    place = models.CharField(max_length=100, verbose_name='受理地区')
    price = models.IntegerField(verbose_name='价格')
    discount = models.CharField(max_length=100, verbose_name='优惠信息')
    discountprice = models.IntegerField(verbose_name='优惠价格')
    orderknow = models.CharField(max_length=100, verbose_name='预订须知')
    slogan = models.ImageField(upload_to='Visa/',
                              blank=True,
                              verbose_name='封面图片')
    flow = models.ImageField(upload_to='Visa/',
                              blank=True,
                              verbose_name='办签流程')
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='取消政策')
    tip = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='温馨提示')
    tips = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='重要提示')
    message = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='产品服务信息')
    views = models.PositiveIntegerField('浏览量', default=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '签证'
        verbose_name_plural = '签证'

class visaAbout(models.Model):
    title = models.ForeignKey(Visa, related_name='abouts', verbose_name='签证名称', on_delete=models.CASCADE, null=True)
    about = models.ImageField(upload_to='Visa/',
                              blank=True,
                              verbose_name='产品介绍')
    class Meta:
        verbose_name = '产品介绍'
        verbose_name_plural = '产品介绍'

class visaData(models.Model):
    PEOPLE_CHOICES = (
        ('在职人员', '在职人员'), ('自由职业', '自由职业'), ('在校学生', '在校学生'),
        ('退休人员', '退休人员'), ('学龄前儿童', '学龄前儿童'),
    )
    title = models.ForeignKey(Visa, related_name='datas', verbose_name='签证名称', on_delete=models.CASCADE, null=True)
    people = models.CharField(choices=PEOPLE_CHOICES, max_length=10, verbose_name='人员类型')
    data = models.CharField(max_length=10, verbose_name='材料名称')
    type = models.CharField(max_length=10, verbose_name='材料类型')
    amount = models.IntegerField(verbose_name='材料数量')
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='材料说明')
    class Meta:
        verbose_name = '所需材料'
        verbose_name_plural = '所需材料'


class Strategy(models.Model):
    title = models.CharField(max_length=20, verbose_name='攻略名称')
    file = models.FileField(upload_to='Strategy/', blank=True, verbose_name='攻略资料')
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='攻略描述')
    photo = models.ImageField(upload_to='Strategy/Img/',
                              blank=True,
                              verbose_name='封面图片')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略'
        verbose_name_plural = verbose_name
        ordering = ['-publishDate']