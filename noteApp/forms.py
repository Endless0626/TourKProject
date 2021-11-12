from django import forms
from .models import Note

class NoteForm(forms.ModelForm):  #建立模型表单类
    class Meta:   #通过元信息类进行模型的定制化
        model = Note  #需要定制化的模型
        fields = ('pagephoto', 'titlephoto', 'title', 'author', 'tripDate',
                  'days', 'people', 'price', 'description')  #需要定制化的字段


# pagephoto = models.ImageField(upload_to='note/', blank=True, null=True, verbose_name='封面图')
# titlephoto = models.ImageField(upload_to='note/', blank=True, null=True, verbose_name='头图')
# title = models.CharField(max_length=50, verbose_name="游记标题")
# author = models.CharField(max_length=10, null=True, verbose_name="作者", default="匿名")
# tripDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='出游时间')
# days = models.CharField(max_length=10, null=True, verbose_name="出游天数")
# people = models.CharField(max_length=20, null=True, verbose_name="人物")
# price = models.CharField(max_length=10, null=True, verbose_name="平均消费")
# description = UEditorField(default='', width=1000, height=1000,
#                            imagePath='note/images/', filePath='note/files/', verbose_name="内容")
# publishDate = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
# views = models.PositiveSmallIntegerField('浏览量', default=0)
