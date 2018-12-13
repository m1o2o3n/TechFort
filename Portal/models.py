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


    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))




# class Author(models.Model):
#     articles = models.ForeignKey(User)
#     author = models.IntegerField(max_length=100, null=True, help_text='u作者')