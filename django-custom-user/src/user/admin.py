from django.contrib import admin
# import the UserAdmin to create a class that will control the admin
# interface and what is displayed.
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# import the NewUser model to register it
from .models import NewUser


class UserAdminConfig(UserAdmin):
    # create a search facility by adding search fields
    search_fields = ('email', 'user_name', 'first_name',)
    # Then we can add a way to filter by staff active, firstname, etc..
    list_filter = ('email', 'user_name' ,'first_name', 'is_active', 'is_staff',)
    ordering = ('-start_date',)
    # create a list display as well:
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff',)


admin.site.register(NewUser)
