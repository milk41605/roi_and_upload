from __future__ import unicode_literals

from django.db import models



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
#
#
#
# class Document_images(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='images/%Y/%m/%d/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
