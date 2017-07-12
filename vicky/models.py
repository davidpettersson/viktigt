from django.db import models


class Alert(models.Model):
    alert_id = models.CharField(max_length=128)
    alert_sender = models.CharField(max_length=128)
    alert_sent = models.DateTimeField()
    message_xml = models.TextField()
    message_sha1sum = models.CharField(max_length=16)
    message_received = models.DateTimeField(auto_now_add=True)
    message_last_presented = models.DateTimeField(auto_now=True)
