from django.contrib.auth.models import AbstractUser
from django.db import models

from libs.kippt import Kippt


class KipptUser(AbstractUser):
    """
    Defines our custom user model and fields

    """
    api_token = models.CharField(max_length=255)
    list_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.username

    def kippt_client(self):
        return Kippt(self.username, api_token=self.api_token)
