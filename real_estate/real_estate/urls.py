from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path("supersecret/", admin.site.urls),
]
+static(settings.MEDIA_ROOT , Document_root = settings.MEDIA_URL)