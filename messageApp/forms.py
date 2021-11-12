from django import forms
from .models import Message

class MessageForm(forms.ModelForm):  #建立模型表单类
    class Meta:   #通过元信息类进行模型的定制化
        model = Message  #需要定制化的模型
        fields = ('name', 'phone', 'email', 'title', 'content')  #需要定制化的字段