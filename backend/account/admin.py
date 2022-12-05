import logging

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import ModelAccountUser
from account.forms import FormAccountUserChange, FormAccountUserAdmin

logger = logging.getLogger(__name__)



@admin.register(ModelAccountUser)
class AdminAccountUser(UserAdmin):
    """
    User Account admin
    """
    form = FormAccountUserChange
    add_form = FormAccountUserAdmin

    list_display = (
        'email','id','first_name','phone_number','uid','is_staff','is_superuser','is_active','created','updated'
    )
    list_filter = ('is_superuser','is_staff','is_active')
    readonly_fields = ('groups',)

    fieldsets = (
        (
            None,
            {
                'fields':
                (
                    'email','password','phone_number'
                )
            }
        ),
        (
            'Personal info',
            {
                'fields':('first_name','last_name')
            }
        ),
        (
            'Permissions',
            {
                'fields':('is_staff','is_superuser','is_active')
            }
        ),
        (
            'Groups',{
                'fields':('groups',)
            }
        )
    )


    add_fieldsets = (
        (
            None,{
                'classes':('wide',),
                'fields':(
                    'email','first_name','last_name','password','confirm_password','is_staff','is_superuser','is_active'
                )
            }
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)