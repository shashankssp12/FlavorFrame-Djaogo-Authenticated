"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import *
from FlavorFrame.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # -----------------HOME (default)-----------------
    path('', home , name='home'),
    path('about/',about , name='about'),
    path('contact/',contact, name='contact'),
    
    # -----------------FLAVORFRAME-----------------
    path('register/' ,register , name='register'),
    path('login/' ,login_page, name='login_page'),
    path('logout/' , logout_page , name='logout_page'),
    path('recipes/',recipes,name='recipes'),
    path('update-recipe/<id>/',update , name='update'),#Dynamic urls
    path('delete-recipe/<id>/',delete , name='delete'),#Dynamic urls
]

#  Serves media files (like uploaded images) only in development mode (DEBUG=True).
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()