from django.db import models
from django.contrib.auth.models import User

import django.utils.timezone as timezone


class Tips(models.Model):
    Tips = models.CharField(max_length=200)


class Articles(models.Model):
    title = models.CharField(max_length=400, null=False, help_text='u标题')
    author = models.ForeignKey(User, on_delete=None)
    tips = models.ForeignKey(Tips, on_delete=None, default=None, null=True)
    content = models.TextField(help_text="u正文")
    createdate = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s' % (self.catname)

