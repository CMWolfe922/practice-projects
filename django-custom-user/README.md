# BUILDING A NEW CUSTOM USER MODEL
---

> This project will extend the User model's fields and use the email as a username. I will also create two forms. One will be the basic registration form, the other will come after the signup/registration form.

> This will make it so that each user can signup/register pretty easily and quickly but also to give them a way to add additional information that will make using whatever app I am building much more dybnamic as far as user information goes.
---


## GIT BRANCH STRUCTURE

1) `master` --> the master branch for the whole practice project repository

1.1) `django-custom-user001` --> This is like the master branch but just for the djagno custom user project. 001 signifies version 1.

1.1.1) `dcu-main ` --> Now this will be used to make it easier to keep track of the "master branch" for django-custom-user. each merge will go to this branch first and then if everything checks out. It will then be merged with the abover branch.

    1.1.2) `user001` --> First user branch. This is the first changes to the user app.

    1.1.3) `user002` --> Second user branch. This will handle the Account Manager.

    1.1.4) `user003` --> Third user branch. This branch is responsible for
    the Account Manageer's ,methods and updating them.

1.2) `django-custom-user002` --> this is the master branch for the django custom user project version 2. Everything up to this point works and has been pushed to the cloud

1.2.1) `dcu-main2` --> This is the slave branch for the `django-custom-user002` that will be used to create more slave branches under. This will be where I start building out the rest of the user app.

    1.2.2) `user-v2.1.1` --> this will be the slave branch that has the first changes to the second version of the user app.

## PROCESS OF BUILDING THE NEW USER MODEL:
---
- step 1: Build the custom User model (One that uses the extended fields/email as username)

- Step 2: Build a model manager:

- Step 3: Build the new user model with extended fields:

- step 4: Customise the Django admin interface:

- step 5: Build Project Tests:


### NOTES & TASKS TO REMEMBER TO UTILIZE THIS MODEL IN OTHER PROJECTS:
---

> I will add examples and other small notes that I think are relevant to being able to replicate this in other projects.

###### Create a django-project inside the django-custom-user directory

```sh
django-admin startproject core
```

- _once the core project is created then change the top level directory to src. I have to remember that this will be one of many proejcts in the practice projects repository. So in order to keep them seperate, I will need to make sure that the project is completely inaccessible from other projects._

so now inside of the django-custom-user project, there is a README file, scripts.py, .gitignore (to ignore certain things from this project), a virtual environment and now the src directory which will contain all of the django app files.
---

> Store this point in the `dcu-main` __git branch__

===

> I created the `user` app as well as a git branch called `user001` where all the first changes will be committed to.

--> Now I need to build the `NewUser` model:

```python
# imports needed:
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class NewUser():
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(_('is user staff'), default=False)
    is_active = models.BooleanField(_('is user active'), default=False)

```

`gettext_lazy` is a way to have strings that are important on the web app be translatable into other languages so that more users have access to my app. Even though the models key won't be transated the description and what type of data is needed can be translated like the rest of the web app.

###### THIS IS VERY IMPORTANT TO MAKE SURE MORE PEOPLE CAN UTILIZE MY APP!

> Now that the model is built. I need to begin thinking about how to integrating this within Django, or telling Django we are using a custom user model. Go to here for DOCS on how to do this!

- [HOW TO LOG A USER IN](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in)

- [HOW TO LOG A USER OUT](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out)

- [GET SIMPLE AUTHENTICATION IN WEB REQUESTS](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authentication-in-web-requests)

- [PERMISSION CACHING](https://docs.djangoproject.com/en/4.0/topics/auth/default/#permission-caching)

===

### Specifying A Custom User Model:

[Click for Docs](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#specifying-a-custom-user-model)

- When you keep all user specific data in one model, you remove the need for more complex database queries that help retrieve relevant models.

- But! it could be more suitable that each app in a Django project have their own customized user specific data (which would then have a relation to the User model). This would allow each app to have their own user specific data requirments without potentially conflicting or breaking assumptions by other apps.

    - to do this I would have to keep the User model as basic as possible. Having it focused on authentication and folowing the minimum requirments Django expects custom user models to meet.

> The easiest way to construct a compliant custom user model is to inherit from [AbstractBaseUser](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser). [AbstractBaseUser](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser) provides the core implementation of a user model, including hashed passwords and tokenized password resets. [You must then provide some key implementation details](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser)

    - to inherit from `AbstractBaseUser` I must import it from the 'auth.models` modules.

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
...

# Then you can place your models here
class NewUser():
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(_('is user staff'), default=False)
    is_active = models.BooleanField(_('is user active'), default=False)

# At the bottom of the models is where you specify the parameters:
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Required fields is the fields that will be prompted when a user trys
    # to create a new superuser
```

* USERNAME_FIELD --> This is the field that will be used to login and out of the account.

* REQUIRED_FIELDS --> This is a list of fields that will be used/prompted whenever a new superuser is created.


### Using the `PermissionsMixin`

---

The permission mixin hooks up the user to the Django permission manager.


### Using the `BaseUserManager`

---

- To use the `BaseUserManager` I need to create a new class. I will create a `CustomAccountManager` and inherit the `BaseUserManager`

```python
from django.contrib.auth.models import BaseUserManager, PermissionMixin, AbstractBaseUser

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
```

> Now that the `CustomAccountManager` is created, I need to add it to the `NewUser` model in the following way:
    - `objects = CustomAccountManager()`


###### BELOW IS THE COMPLETE `models.py` FILE FOR THE USER APP:
---

```python
from django.db import models
from django.utils import timezone
# This helps with translating strings into other languages around the world
from django.utils.translation import gettext_lazy as _
# importing the AbstractBaseUser and BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    # I need to add the first_name and user_name fields here
    REQUIRED_FIELDS = ['user_name']

    # Now create a dunder method for __str__ to print the new users username
    def __str__(self):
        return f"{self.user_name}: {self.email}"

```

===

Now that the models file is setup. I will have to make changes to the projects `settings.py` file:

> in the `settings.py` file I added the following changes:
> `AUTH_USER_MODEL = 'user.NewUser'`

- I also added the `'user'` app to the app list.

===
