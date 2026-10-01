from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = (
        "__str__",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
        )
    list_editable = ("is_active","is_staff",)
    
    list_filter = ("is_active","is_staff","is_superuser","date_joined","last_login")
    
    list_per_page = 20

    date_hierarchy = "date_joined"
    
    search_fields = ("display_name","first_name","last_name","username")

    empty_value_display = "----"

    # add_form = UserCreationForm
    
    # form = UserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )
    
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email","phone_number")
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": (("first_name","last_name",),)
            },
        ),
        (
            "گزینه های پیشرفته",
            {
                "classes": ("collapse",),
                "fields": ("groups","user_permissions")
            },
        ),
        (
            "تاریخ ها",
            {
                "classes": ("wide",),
                "fields": ("date_joined","last_login",)
            },
        ),
    )
    
    readonly_fields = ("date_joined","last_login")