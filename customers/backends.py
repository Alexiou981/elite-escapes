from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in using either
    their username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        # Check if user exists by email or username
        user = (
            UserModel.objects.filter(email=username).first() or
            UserModel.objects.filter(username=username).first()
        )

        if user and user.check_password(password):
            return user
        return None
