import django.urls

import checking.views

urlpatterns = [
    django.urls.path('', checking.views.about),
]
