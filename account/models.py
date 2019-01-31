from django.db import models
from django.utils import timezone


# Create your models here.
class Account (models.Model):
    #id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30, default='')
    lastName = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=32, default='some@ema.il')
    middleName = models.CharField(max_length=30, default='')
    creationTime = models.DateTimeField(default=timezone.now())
    phoneNumber = models.CharField(max_length=20, default='')
    profilePic = models.CharField(max_length=50, default='')
    lastLogin = models.DateTimeField(default=timezone.now())
    registrationToken = models.CharField(max_length=50, default='')
    rating = models.FloatField(default=5.0)
    IdCard = models.CharField(max_length=50, default='123456')
    enablePrivacy = models.BooleanField(default=True)
    userTypeId = models.SmallIntegerField(default=1)
    verificationId = models.SmallIntegerField(default=0)
    googleId = models.CharField(max_length=50, default='    ')
    avatar = models.CharField(max_length=250, default='default.jpg')

    def __str__(self):
        return self.lastName + ' ' + self.firstName + " " + self.email




