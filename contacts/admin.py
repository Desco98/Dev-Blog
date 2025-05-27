from django.contrib import admin
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'sent_at']
    list_display_links = ['id', 'name']


admin.site.register(Contacts, ContactAdmin)