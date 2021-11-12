from django.db import models
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名字')
    enname = models.CharField(max_length=40, verbose_name='城市罗马音')
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='城市描述')
    photo = models.ImageField(upload_to='City/',
                              blank=True,
                              verbose_name='城市照片')
    views = models.PositiveIntegerField('浏览量', default=100)
    class Meta:
        verbose_name = '热门城市'
        verbose_name_plural = '热门城市'

class Special(models.Model):
    SPECIAL_CHOICES = (('景点', '景点'), ('娱乐', '娱乐'), ('美食', '美食'),)
    title = models.CharField(max_length=50, verbose_name='特色标题')
    kname = models.CharField(max_length=20, verbose_name='韩文名字')
    place = models.CharField(max_length=20, blank=True, null=True, verbose_name='所处城市')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='具体地址')
    score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, verbose_name='特色评分')
    description = models.TextField(max_length=500, verbose_name='特色详情描述')
    tickets = models.TextField(verbose_name='门票', blank=True, null=True)
    traffic = models.TextField(verbose_name='交通路线', blank=True, null=True)
    open = models.TextField(verbose_name='开放时间', blank=True, null=True)
    specialType = models.CharField(choices=SPECIAL_CHOICES, max_length=50, verbose_name='特色类型')
    publishDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
    comment1 = models.TextField(max_length=500, verbose_name='精选点评1')
    Date1 = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='点评时间1')
    comment2 = models.TextField(max_length=500, verbose_name='精选点评2')
    Date2 = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='点评时间2')
    comment3 = models.TextField(max_length=500, verbose_name='精选点评3')
    Date3 = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='点评时间3')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '特色'
        verbose_name_plural = '特色'
        ordering = ('-publishDate', )

class SpecialImg(models.Model):
    special = models.ForeignKey(Special, related_name='specialImgs', verbose_name='特色', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Special/', blank=True, verbose_name='特色照片')

    class Meta:
        verbose_name = '特色图片'
        verbose_name_plural = '特色图片'