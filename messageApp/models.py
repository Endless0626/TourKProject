from django.db import models
from django.utils import timezone

class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name='昵称')
    phone = models.CharField(max_length=20, verbose_name='电话号码')
    email = models.EmailField(max_length=30, verbose_name='邮箱')
    title = models.CharField(max_length=40, verbose_name='留言标题')
    content = models.CharField(max_length=200, verbose_name='留言内容')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='提交时间')
    replycontent = models.TextField(blank=True, null=True, verbose_name='回复')
    replyDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='回复时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-replyDate']

class Protocol(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='简称')
    content = models.TextField(verbose_name='内容')
    file = models.FileField(upload_to='Protocol/', blank=True, verbose_name='协议资料')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='提交时间')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '协议'
        verbose_name_plural = verbose_name
        ordering = ['-publishDate']
