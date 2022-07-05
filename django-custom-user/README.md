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


### Using the `PermissionMixin`

---

The permission mixin hooks up the user to the Django permission manager.


### Using the `BaseUserManager`

---

- To use the `BaseUserManager` I need to create a new class. I will create a `CustomAccountManager` and inherit the `BaseUserManager`

```python

from django.contrib.auth.models import BaseUserManager, PermissionMixin, AbstractBaseUser

class CustomAccountManager(BaseUserManager):

    # create a method for what happens when creating a new user:
    def create_user():

```
