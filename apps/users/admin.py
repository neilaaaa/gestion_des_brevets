from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('nom_role',)
    search_fields = ('nom_role',)


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):

    list_display = ('username', 'email', 'role', 'is_staff', 'date_ajout')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'email', 'role', 'date_ajout')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Dates importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # ⚠️ IMPORTANT (fix create user bug)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('date_ajout',)