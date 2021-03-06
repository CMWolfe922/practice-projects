from django.db import models
from django.utils import timezone
# This helps with translating strings into other languages around the world
from django.utils.translation import gettext_lazy as _
# importing the AbstractBaseUser and BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.contrib.auth.mixins import PermissionMixin

# Create the CustomAccountManager class
class CustomAccountManager(BaseUserManager):

    # Method for what happens when a new user is created
    def create_user(self, email, user_name, first_name, password, **other_fields):
        """
        The params are for what will be required. Examples: enail, user_name, password,
        first_name, password, **other_fields
        """
        # Adding a validation check for the user's email
        if not email:
            raise ValueError(_("You must provide and email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)

        # now create a way to set password
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        # When creating the superuser we will utilize the **other_fields parameter
        # to set the is_staff and is_superuser to True
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        # These validations can be used in Testing
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, user_name, first_name, password, **other_fields)


# Now I have to inherit AbstractBaseUser into my NewUser model
class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(_('is user staff'), default=False)
    is_active = models.BooleanField(_('is user active'), default=False)

    # setting up the CustomAccountManager
    objects = CustomAccountManager()

    # setting the first parameter
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    # Now create a dunder method for __str__ to print the new users username
    def __str__(self):
        return f"{self.user_name}: {self.email}"
