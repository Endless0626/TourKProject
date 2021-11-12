import xadmin
from .models import Note

# style_fields = {'detail': 'ueditor'}

class NoteAdmin(object):
    list_display = ('title', 'author', 'publishDate', 'views')
    style_fields = {'description': 'ueditor'}

xadmin.site.register(Note, NoteAdmin)