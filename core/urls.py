from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import ConcatView, DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="market-dashboard"),
    path("admin/", admin.site.urls),
    path("contact/", ConcatView.as_view(), name="market-contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()

