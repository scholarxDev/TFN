from django.contrib import admin
from .models import Newsletter


# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):

    pass


admin.site.register(Newsletter, NewsletterAdmin)