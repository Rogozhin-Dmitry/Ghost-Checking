import django.urls

import checking.views

app_name = 'checking'

urlpatterns = [
    django.urls.path('', checking.views.UploadFile.as_view(), name='upload_file'),
]
