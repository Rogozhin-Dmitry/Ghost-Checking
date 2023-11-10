import django.urls

import loading.views

app_name = 'loading'

urlpatterns = [
    django.urls.path('<int:a>', loading.views.progres, name='progres-bar'),
]
