from django.contrib import admin
from .models import Profile, Skill, Project, ContactInfo, AboutContent
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at', 'updated_at')
    search_fields = ('name', 'title')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    search_fields = ('name',)
    ordering = ('-percentage',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'updated_at')
    search_fields = ('email', 'phone', 'address')

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title', 'content')

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
