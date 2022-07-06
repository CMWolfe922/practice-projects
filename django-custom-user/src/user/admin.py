from django.contrib import admin
# import the NewUser model to register it
from .models import NewUser

admin.site.register(NewUser)
