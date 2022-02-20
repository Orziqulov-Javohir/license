
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "Организация Нур Транс"
admin.site.site_title = "Нур Транс"
admin.site.index_title = "Панель администратора Нур Транс"


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
