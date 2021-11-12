from django.utils import timezone
from django.db import models
from django import forms

# 名字，英文，评分，城市，地址，入住时间，离店时间，建成于
# 酒店规模，附近景点，酒店攻略，出行提示
# 主要设施（多选），酒店服务（多选），酒店设施（多选），房间设施（多选）
# 历史房型房价(房型，房价，人数)
# 图片（外观、内景、房间、环境、餐厅）
# 用户评论（姓名，推荐指数，评论，时间，图片）

class MainFacility(models.Model):
    facilities = models.CharField(max_length=20, verbose_name='设施内容')

    def __str__(self):
        return self.facilities

    class Meta:
        verbose_name = '主要设施'
        verbose_name_plural = '主要设施'

class Service(models.Model):
    facilities = models.CharField(max_length=20, verbose_name='酒店服务')

    def __str__(self):
        return self.facilities

    class Meta:
        verbose_name = '酒店服务'
        verbose_name_plural = '酒店服务'

class HotelFacility(models.Model):
    facilities = models.CharField(max_length=20, verbose_name='酒店设施')

    def __str__(self):
        return self.facilities

    class Meta:
        verbose_name = '酒店设施'
        verbose_name_plural = '酒店设施'

class RoomFacility(models.Model):
    facilities = models.CharField(max_length=20, verbose_name='房间设施')

    def __str__(self):
        return self.facilities

    class Meta:
        verbose_name = '房间设施'
        verbose_name_plural = '房间设施'

class Hotel(models.Model):
    title = models.CharField(max_length=20, verbose_name='酒店名字')
    entitle = models.CharField(max_length=50, verbose_name='英文名字')
    score = models.FloatField(max_length=10, verbose_name='酒店评分')
    city = models.CharField(max_length=10, verbose_name='所在城市')
    address = models.CharField(max_length=50, verbose_name='地址')
    checkin = models.CharField(max_length=50, verbose_name='入住时间')
    checkout = models.CharField(max_length=50, verbose_name='离店时间')
    year = models.IntegerField(null=True, blank=True, verbose_name='建成年份')
    scale = models.CharField(max_length=50, null=True, blank=True, verbose_name='酒店规模')
    near1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='附近景点1')
    near2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='附近景点2')
    near3 = models.CharField(max_length=20, null=True, blank=True, verbose_name='附近景点3')
    method = models.TextField(null=True, blank=True, verbose_name='酒店攻略')
    tip = models.TextField(null=True, blank=True, verbose_name='出行提示')

    mfacility = models.ManyToManyField(MainFacility, verbose_name='主要设施')
    service = models.ManyToManyField(Service, verbose_name='酒店服务')
    hfacility = models.ManyToManyField(HotelFacility, verbose_name='酒店设施')
    rfacility = models.ManyToManyField(RoomFacility, verbose_name='房间设施')

    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '酒店'
        verbose_name_plural = '酒店'
        ordering = ('-views', )

class RoomPrice(models.Model):
    title = models.ForeignKey(Hotel, related_name='roomPrice', verbose_name='历史房型房价', on_delete=models.CASCADE)
    roomType = models.CharField(max_length=20, null=True, blank=True, verbose_name='房型')
    roomPeople = models.CharField(max_length=20, null=True, blank=True, verbose_name='可住人数')
    roomPrice = models.CharField(max_length=20, null=True, blank=True, verbose_name='房价')

class HotelImgs(models.Model):
    PHOTO_CHOICES = (
        ('外观', '外观'), ('内景', '内景'), ('房间', '房间'),
        ('环境', '环境'), ('餐厅', '餐厅'), ('其他', '其他'),
    )
    title = models.ForeignKey(Hotel, related_name='hotelImgs', verbose_name='酒店图片', on_delete=models.CASCADE)
    photoType = models.CharField(choices=PHOTO_CHOICES, max_length=50, verbose_name='图片类型')
    photo = models.ImageField(upload_to='Hotel/Comment/', blank=True, verbose_name='评价图片')

class UserComment(models.Model):
    title = models.ForeignKey(Hotel, related_name='userComment', verbose_name='用户评价', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户昵称')
    content = models.TextField(null=True, blank=True, verbose_name='评价内容')
    index = models.IntegerField(null=True, blank=True, verbose_name='评价指数')
    commentDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')






