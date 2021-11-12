from django import forms
from .models import Quiz, Reply

class QuizForm(forms.ModelForm):  #建立模型表单类
    class Meta:   #通过元信息类进行模型的定制化
        model = Quiz  #需要定制化的模型
        fields = ('name', 'title', 'content')  #需要定制化的字段

class ReplyForm(forms.ModelForm):  #建立模型表单类
    class Meta:   #通过元信息类进行模型的定制化
        model = Reply  #需要定制化的模型
        fields = ('replyname', 'title', 'replycontent')  #需要定制化的字段