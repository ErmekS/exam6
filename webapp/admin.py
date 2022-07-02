from django.contrib import admin

# Register your models here.
from webapp.models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'entry', 'created_time', 'updated_time', 'status']
    list_display_links = ['entry']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['entry', 'status', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Guestbook, GuestbookAdmin)
