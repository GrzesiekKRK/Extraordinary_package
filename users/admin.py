from django.contrib import admin

from .models import CustomUser, Employee


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "is_active",
        "date_joined",
    ]
    list_filter = ["role", "is_active", "date_joined"]
    ordering = ["-date_joined"]
    search_fields = ["email", "username", "first_name", "last_name"]
    list_per_page = 25


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
                    "department",
                    "driver",
                    "driver_semi",
                    "on_route"
                ]
    search_fields = ["department", "driver", "driver_semi", "on_route"]
    ordering = ["department"]
    list_per_page = 25


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
