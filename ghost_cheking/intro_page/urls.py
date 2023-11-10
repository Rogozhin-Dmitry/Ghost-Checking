import django.urls

import intro_page.views

urlpatterns = [
    django.urls.path('', intro_page.views.intro, name='intro'),
]
