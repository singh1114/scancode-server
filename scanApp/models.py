from __future__ import unicode_literals
from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
class UserInfo(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    total_files_scanned = models.PositiveIntegerField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class codebase(models.Model):
    def __str__(self):
        return self.url

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.CharField(max_length=3000)
    file_number = models.IntegerField(null=True, blank=True)
    codebase_size = models.IntegerField(null=True, blank=True, default=0)


class results(models.Model):
    def __str__(self):
        return self.total_errors

    codebase = models.ForeignKey(codebase)
    scanned_files = models.IntegerField(null=True, blank=True, default=0)
    total_errors = models.IntegerField(null=True, blank=True, default=0)
    scan_time = models.IntegerField(null=True, blank=True, default=0)
    scan_info = models.CharField(max_length=3000)


class file_scanned_info(models.Model):
    def __str__(self):
        return str(self.user_one) + '-' + str(self.user_two)

    codebase = models.ForeignKey(codebase)
    file_name = models.CharField(max_length=3000)
    file_scanned_info = models.CharField(max_length=3000)


class license_and_copyrights(models.Model):
    def __str__(self):
        return str(self.license_name.count())

    file_scanned_info = models.ForeignKey(file_scanned_info)
    license_name = models.CharField(max_length=3000)
    license_info = models.CharField(max_length=3000)