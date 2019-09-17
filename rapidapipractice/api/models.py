from django.db import models

class Album(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    musician = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        ordering = ['date_created']