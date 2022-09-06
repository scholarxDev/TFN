from django.contrib import admin
from .models import Organization, Carousel, Asset

class CarouselInline(admin.StackedInline):
    '''Stacked Inline View for Carousel'''
    model = Carousel


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'subdomain_prefix',)
    inlines = (CarouselInline,)

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Carousel)
admin.site.register(Asset)