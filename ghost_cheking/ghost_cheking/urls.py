import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.contrib.staticfiles.urls
import django.urls
from django.contrib import admin
from django.urls import path, include

import checking.urls
import intro_page.urls
import results.urls
import loading.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(intro_page.urls)),
    path('check/', include(checking.urls)),
    path('result/', include(results.urls)),
    path('load/', include(loading.urls))

]

if django.conf.settings.DEBUG:
    if django.conf.settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    urlpatterns += django.contrib.staticfiles.urls.staticfiles_urlpatterns()

if django.conf.settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        django.urls.path(
            '__debug__/',
            django.urls.include(debug_toolbar.urls),
        ),
    )
