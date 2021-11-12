from django.shortcuts import render
from .forms import MessageForm
from .models import Message, Protocol
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse, JsonResponse
import os

def message(request):
    if request.method == 'POST':
        messageForm = MessageForm(data=request.POST) #创建模型表单对象
        if messageForm.is_valid():
            messageForm.save() #存到数据库
            return render(request, 'successm.html')
    else:  #没有提交
        messageForm = MessageForm()  #创建模型表单对象，并传给message.html
    return render(
        request, 'message.html', {
            'messageForm': messageForm,
        })

def showreply(request):
    replyList = Message.objects.filter(replycontent__isnull=False)  # 得到 有回复 的记录
    return render(request, 'showreply.html', {
        'replyList': replyList
    })

def about(request):
    protocolList = Protocol.objects.all().order_by('publishDate')
    return render(request, 'about.html', {
        'protocolList': protocolList,
    })

def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break

def getDoc(request, id):
    doc = get_object_or_404(Protocol, id=id)
    update_to, filename = str(doc.file).split('/')
    filepath = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response
