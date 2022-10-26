from django.contrib import admin
from django.urls import path
from zuri.views import Home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

