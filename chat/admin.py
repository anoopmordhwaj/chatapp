from django.contrib import admin
from chat.models import Room, Message, UploadDp, Recents

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(UploadDp)
admin.site.register(Recents)