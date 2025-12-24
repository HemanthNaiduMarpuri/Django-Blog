from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm as DjangoUserChangeForm
from django import forms
from .models import User, Blog


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('admin', 'Blog Admin'),
        ('user', 'User'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        if role == "admin":
            user.is_admin = True
            user.is_staff = True
            user.is_user = False
        else:
            user.is_admin = False
            user.is_user = True
            user.is_staff = False
        if commit:
            user.save()
        return user


class CustomUserChangeForm(DjangoUserChangeForm):
    ROLE_CHOICES = (
        ('admin', 'Blog Admin'),
        ('user', 'User'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['role'].initial = 'admin' if self.instance.is_admin else 'user'

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        if role == "admin":
            user.is_admin = True
            user.is_user = False
            user.is_staff = True
        else:
            user.is_admin = False
            user.is_user = True
            user.is_staff = False
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ("username", "email", "role", "is_admin", "is_staff", "is_superuser")
    list_filter = ("is_admin", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "email", "role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "username")
    ordering = ("email",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at", "author")
    ordering = ("-created_at",)

    readonly_fields = ('image_preview', )

    fieldsets = (
        (None, {
            'fields' : ("title", "content", "image", "image_preview", "author"),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" style="border-radius:8px;" />'
        return 'No Image'
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"


admin.site.register(User, CustomUserAdmin)

