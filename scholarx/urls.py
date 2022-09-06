"""scholarx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import auth


admin.site.site_header = 'ScholarX admin'
admin.site.site_title = 'ScholarX admin'
admin.site.index_title = 'ScholarX administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('xpro.urls')),
    path('', include('photo.urls')),
    path('', include("newsletter.urls")),
    path('', include('django.contrib.auth.urls')),
    path('', include('pwa.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path("blog/", include("blog.urls")),
    path("village/", include("village.urls")),
    path("scholarship/", include("scholarship.urls")),
    path("campaign/", include("campaign.urls")),
    path("payment/", include("payment.urls")),
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

