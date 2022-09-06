from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Student, School, Sponsor


# Register your models here.
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'first_name', 'last_name', 'organization']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['date_joined']


class StudentAdmin(admin.ModelAdmin):

    pass


class SchoolAdmin(admin.ModelAdmin):

    pass


class SponsorAdmin(admin.ModelAdmin):

    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Sponsor, SponsorAdmin)

admin.site.unregister(Group)

