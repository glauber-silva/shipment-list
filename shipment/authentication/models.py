import jwt
from datetime import timedelta, datetime
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    """
    this is will override create_user  function which we will use  to create
     'USER" objects
    """

    def create_user(self, username, email, password=None):
        """
        Create and return a 'User' with an email , username,  and password
        :param username: Unique string entered by the user
        :param email: Unique email string entered by the user
        :param password: Alphanumeric value entered by the user
        :return: A object User
        """
        if username is None:
            raise TypeError("User must have a username")

        if email is None:
            raise TypeError("User must have an email address")

        if password is None:
            raise TypeError("User must have a password ")

        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a 'User' with superuser (admin) permissions.
        :param username: Unique string value entered by user
        :param email: Unique email string entered by user
        :param password: Alphanumeric value entered by user
        :return: Returns a User object
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Class to represent a User in the app
    """
    username = models.CharField(db_index=True, max_length=20, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Since we do not store the user's real name, we return their username
        instead.
        """
        return self.username

    def get_short_name(self):
        """
         Since we do not store the user's real name, we return their username
         instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has
        an expiry date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')