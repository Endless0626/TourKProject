from django.db import models

class Ad(models.Model):

    title = models.CharField(max_length=20,null=True, blank=True, verbose_name='图片标题')
    photo = models.ImageField(upload_to='Home/Img/',
                              blank=True,
                              verbose_name='首页轮播图片')

    class Meta:
        verbose_name = '首页图片'
        verbose_name_plural = '首页图片'