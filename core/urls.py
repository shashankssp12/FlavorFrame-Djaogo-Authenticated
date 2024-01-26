"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from home.views import *
from VEG_REC.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', home , name='home'),
    path('delete-recipe/<id>/',delete , name='delete'),#Dynamic urls
    path('update-recipe/<id>/',update , name='update'),
    path('recipes/',recipes,name='recipes'),
    path('about/',about , name='about'),
    path('contact/',contact, name='contact'),
    # path('page2/', page2, name='page2'),
    path('admin/', admin.site.urls),
    path('login/' ,login_page, name='login_page'),
    path('register/' ,register , name='register'),
    path('logout/' , logout_page , name='logout_page')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()