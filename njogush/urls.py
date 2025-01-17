"""
URL configuration for njogush project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
# from django.conf.urls.static import static
from .static import static # Using this version inorder to override debug limitation

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path("chat/", include("chat.urls")),
    path('', include('build_tool.urls')),
]

# ! IMPORTANT: Set DEBUG=True inorder for this to work for pyinstaller compiled version
# TODO https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# TODO https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)