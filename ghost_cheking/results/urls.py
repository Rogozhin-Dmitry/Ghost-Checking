import django.urls

import results.views

app_name = 'results'

urlpatterns = [
    django.urls.path('errors', results.views.errors, name='errors'),
    django.urls.path('all_done', results.views.all_done, name='all_done'),
]
