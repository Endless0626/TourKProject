from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

class Note(models.Model):
    pagephoto = models.ImageField(upload_to='note/', blank=True, null=True, verbose_name='封面图')
    titlephoto = models.ImageField(upload_to='note/', blank=True, null=True, verbose_name='头图')
    title = models.CharField(max_length=50, verbose_name="游记标题")
    author = models.CharField(max_length=10, null=True, verbose_name="作者", default="匿名")
    tripDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='出游时间')
    days = models.CharField(max_length=10, null=True, verbose_name="出游天数")
    people = models.CharField(max_length=20, null=True, verbose_name="人物")
    price = models.CharField(max_length=10, null=True, verbose_name="平均消费")
    description = UEditorField(default='', width=1000, height=1000,
                               imagePath='note/images/', filePath='note/files/', verbose_name="内容")
    publishDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
    views = models.PositiveSmallIntegerField('浏览量', default=0)
    # photo = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='展报')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = '游记'
        verbose_name_plural = verbose_name

