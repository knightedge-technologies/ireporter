from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Redflag(models.Model):
    redflag_title = models.CharField(max_length=100)
    redflag_comment = models.TextField()
    redflag_date = models.DateTimeField(default=timezone.now)
    redflag_status = models.CharField(max_length=200, default='pending')
    redflag_image = models.TextField()
    redflag_video = models.TextField()
    redflag_createdby = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='redflag')
    redflag_location = models.CharField(max_length=200)
