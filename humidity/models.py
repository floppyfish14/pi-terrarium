from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime

now = timezone.localtime(timezone.now())

@python_2_unicode_compatible
class Humidity(models.Model):
    Humidity_Percent = models.IntegerField()
    reading_time = models.DateTimeField('date output')
    def __int__(self):
        return self.Humidity_Percent
    def __unicode__(self):
        return self.reading_time
    def was_output_recently(self):
        return now - datetime.timedelta(days=1) <= self.reading_time <= now
    def was_output_this_hour(self):
        return now - datetime.timedelta(hours=1) <= self.reading_time <= now

# Create your models here.
