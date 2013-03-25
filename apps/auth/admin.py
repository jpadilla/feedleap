from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import KipptUser


class KipptUserAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'email',
        'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(KipptUserAdmin, self).__init__(*args, **kwargs)

        self.fieldsets += (
            ('Other info', {
                'fields': ('api_token', 'list_id')}
             ),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'api_token', 'first_name',
                       'last_name', 'email', 'list_id')}
         ),
    )

admin.site.register(KipptUser, KipptUserAdmin)
