from django.contrib import admin
from django.urls import path, include

import checking.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(checking.urls))
]