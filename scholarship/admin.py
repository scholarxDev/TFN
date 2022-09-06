
from django.contrib import admin
from scholarship.models import *

# Register your models here.


class ScholarshipAdmin(admin.ModelAdmin):

    list_display = ['name', 'country', 'award','deadline']
    search_fields = ['name', 'country', 'award',]


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name',]
    search_fields = ['name',]


class CollegeAdmin(admin.ModelAdmin):

    list_display = ['name',]
    search_fields = ['name',]



admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(College, CollegeAdmin)