from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'author', 'email', 'slug']


admin.site.register(Message, MessageAdmin)
