from django.contrib.auth.backends import ModelBackend

from .models import KipptUser


class KipptUserBackend(ModelBackend):
    def authenticate(self, username=None, api_token=None):
        try:
            return KipptUser.objects.get(username=username, api_token=api_token)
        except KipptUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return KipptUser.objects.get(pk=user_id)
        except KipptUser.DoesNotExist:
            return None
