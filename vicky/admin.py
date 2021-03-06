from django.contrib import admin
from vicky.models import Alert


class AlertAdmin(admin.ModelAdmin):
    date_hierarchy = 'message_received'
    list_display = [ 'alert_id', 'alert_sender', 'alert_sent', 'message_received', 'message_last_presented']


admin.site.register(Alert, AlertAdmin)
