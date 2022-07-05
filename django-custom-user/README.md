# BUILDING A NEW CUSTOM USER MODEL
---

> This project will extend the User model's fields and use the email as a username. I will also create two forms. One will be the basic registration form, the other will come after the signup/registration form.

> This will make it so that each user can signup/register pretty easily and quickly but also to give them a way to add additional information that will make using whatever app I am building much more dybnamic as far as user information goes.
---

---

## PROCESS OF BUILDING THE NEW USER MODEL:
---
- step 1: Build the custom User model (One that uses the extended fields/email as username)

- Step 2: Build a model manager:

- Step 3: Build the new user model with extended fields:

- step 4: Customise the Django admin interface:

- step 5: Build Project Tests:


---


### NOTES & TASKS TO REMEMBER TO UTILIZE THIS MODEL IN OTHER PROJECTS:
---

> I will add examples and other small notes that I think are relevant to being able to replicate this in other projects.

###### Create a django-project inside the django-custom-user directory

```sh
django-admin startproject core
```

- _once the core project is created then change the top level directory to src. I have to remember that this will be one of many proejcts in the practice projects repository. So in order to keep them seperate, I will need to make sure that the project is completely inaccessible from other projects._