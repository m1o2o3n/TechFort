from django.db import models

class Userkey(models.Model):
    lname = models.CharField(max_length=200, null=False)
    lpwd = models.CharField(max_length=200, null=False)


class UserInfo(models.Model):
    name = models.CharField(max_length=200, null=False)
    sex = models.BooleanField()
    mail = models.EmailField()

