from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "is_staff", )
    list_filter = ("username", "email", "is_staff")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "username", "email", "password", "telephone", "type")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "telephone",
                    "type",
                ),
            },
        ),
    )
    search_fields = ("first_name", "last_name", "email", "username")
    ordering = ("-created_at",)


admin.site.register(User, CustomUserAdmin)
