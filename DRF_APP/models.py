from django.db import models


class UserReg(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    photo = models.ImageField(upload_to='photos', max_length=250)
