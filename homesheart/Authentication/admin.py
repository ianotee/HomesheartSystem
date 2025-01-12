from django.contrib import admin
from .models import LoginBackgroundVideo,RegisterBackgroundVideo,User
admin.site.site_header = "Homesheart Admin" 
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'role', 'is_active', 'is_staff']
    list_filter = ['is_staff', 'is_active', 'role']
    search_fields = ['email', 'username']
    ordering = ['email']

    # Fields to display in the user detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'contact', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to display when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role', 'is_active', 'is_staff'),
        }),
    )

admin.site.register(User, CustomUserAdmin)


'''
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_active', 'is_staff')
'''

@admin.register(LoginBackgroundVideo)
class LoginBackgroundVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at')



@admin.register(RegisterBackgroundVideo)
class RegisterBackgroundVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at')

